#!/usr/bin/env python3
"""Realistic RoboEye eyeball: white sclera + black iris/pupil (two filaments).

Same outer dimensions and mounting as cad/eyeFront.kcl:
  * R40 outer / R38.2 inner shell, open rear plane 7 mm in front of the centre
  * four rear blind screw bosses R2.8 with R0.85 pilot holes, 5 mm deep
The separate black pupil (cad/pupil.kcl) and its M2 screw are not needed:
iris and pupil are part of the eyeball itself.

The colour split is a horizontal plane in print orientation (front up), so the
eyeball can be printed either
  * with a multi-material unit (white + black STL loaded as one multi-part object), or
  * on a single nozzle by changing to black filament at the colour-change height.
Every recess of the iris stays at least MIN_BLACK above that plane, so no white
can show through, and nothing protrudes beyond the R40 sphere (lid clearance
unchanged).

The iris is a smooth height field: radial trabeculae, zig-zag collarette,
crenellated pupil margin, crypts and contraction furrows, sitting in a gently
domed recess behind the sphere surface like a real iris behind the cornea.
The pupil is a 12.8 mm well, about 3.2 mm deep, so it reads darker than the iris.

Run:  python3 tools/generate_realistic_eye.py
Requires: numpy, manifold3d
"""
from __future__ import annotations

import json
import math
import struct
from pathlib import Path

import numpy as np
import manifold3d as mf

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exports" / "realistic-eye"

# ---------------------------------------------------------------- dimensions
# Local frame: origin = eye centre, +Z = viewing direction (print "up"),
# +Y = up in the assembly.  Assembly = (X, -Z, Y) + (0, 0, 145).
R_OUT = 40.0            # outer sphere (eyeFront.kcl outerRadius)
R_IN = 38.2             # inner sphere (eyeFront.kcl innerRadius)
REAR_PLANE = 7.0        # open back, 7 mm in front of the centre (rearPlane)
BOSS_R = 2.8            # rear screw bosses (bossA..D)
BOSS_Z = (18.0, 24.0)
PILOT_R = 0.85          # mountPilotRadius
PILOT_Z = (17.0, 23.0)  # 5 mm blind depth from the boss face at Z 18
BOSS_XY = [(-28.0, -8.0), (28.0, -8.0), (-28.0, 8.0), (28.0, 8.0)]

# Plate placement identical to cad/printPlate03White.kcl
PLATE_OFFSET = np.array([128.0, 128.0, -REAR_PLANE])

# Colour split (black above). Plate height = Z_SPLIT - 7 mm = 28.0 mm.
Z_SPLIT = 35.0
R_LIMBUS = math.sqrt(R_OUT**2 - Z_SPLIT**2)    # visible black edge, ~19.37 mm
MIN_BLACK = Z_SPLIT + 0.25                     # lowest allowed iris/pupil floor

# Iris / pupil (scaled from a human eye: iris ~49 %, pupil ~1/3 of the iris)
R_STEP = 17.9           # outer edge of the recessed iris
STEP_DEPTH = 0.35       # recess depth at that edge
R_BLEND = 18.85         # recess runs out smoothly into the sphere here
IRIS_APEX = 38.5        # iris base surface on the axis (1.5 mm behind the sphere)
R_PUPIL = 6.4           # pupil radius (D 12.8 mm)
PUPIL_FLOOR = 36.3      # pupil well floor
LID_MARGIN = 0.12       # relief stays this far inside the R40 sphere
SIMPLIFY_TOL = 0.008    # mesh decimation tolerance for the black part (mm)

SEGMENTS = 256          # revolve resolution of the white shell
ARC_STEP_DEG = 0.6      # profile resolution on spheres
IRIS_SEGMENTS = 1024    # angular resolution of the iris height field
IRIS_DR = 0.05          # radial resolution of the iris height field

rng = np.random.default_rng(20261104)


def sphere_z(r, radius=R_OUT):
    return np.sqrt(np.maximum(radius**2 - np.square(r), 0.0))


def _iris_base_radius():
    h = IRIS_APEX - (float(sphere_z(R_STEP)) - STEP_DEPTH)
    return (R_STEP**2 + h**2) / (2 * h)


R_BASE = _iris_base_radius()


def iris_base(r):
    """Gently domed iris plane, recessed behind the R40 'cornea' sphere.
    Between R_STEP and R_BLEND it runs out smoothly into the sphere."""
    r = np.asarray(r, dtype=float)
    base = IRIS_APEX - (R_BASE - np.sqrt(R_BASE**2 - np.square(np.minimum(r, R_STEP))))
    t = np.clip((r - R_STEP) / (R_BLEND - R_STEP), 0.0, 1.0)
    z0, z1 = IRIS_APEX - (R_BASE - math.sqrt(R_BASE**2 - R_STEP**2)), float(sphere_z(R_BLEND))
    return np.where(r <= R_STEP, base, z0 + (z1 - z0) * t * t * (3 - 2 * t))


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


# ------------------------------------------------------------------ helpers
def ccw(poly):
    poly = np.asarray(poly, dtype=float)
    x, y = poly[:, 0], poly[:, 1]
    area = 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)
    return poly if area > 0 else poly[::-1]


def revolve(profile, segments=SEGMENTS):
    """Revolve an (r, z) polygon around the Z axis."""
    return mf.Manifold.revolve(mf.CrossSection([ccw(profile)]), segments)


def arc_points(radius, z_from, z_to):
    """Points (r, z) on a sphere meridian from height z_from to z_to.
    Uses a global angle grid, so neighbouring bodies share identical vertices."""
    a0 = math.degrees(math.asin(min(z_from / radius, 1.0)))
    a1 = math.degrees(math.asin(min(z_to / radius, 1.0)))
    lo, hi = sorted((a0, a1))
    grid = [k * ARC_STEP_DEG for k in range(int(lo / ARC_STEP_DEG) + 1, int(math.ceil(hi / ARC_STEP_DEG)))]
    angles = [lo] + [g for g in grid if lo + 1e-6 < g < hi - 1e-6] + [hi]
    if a0 > a1:
        angles = angles[::-1]
    return [(radius * math.cos(math.radians(a)), radius * math.sin(math.radians(a))) for a in angles]


# ----------------------------------------------------------- white sclera
def white_shell_untrimmed():
    """Exact eyeFront.kcl geometry, closed at the front (no pupil bore)."""
    outer = arc_points(R_OUT, REAR_PLANE, R_OUT)          # rear rim -> apex
    inner = arc_points(R_IN, R_IN, REAR_PLANE)            # apex -> rear rim
    shell = revolve(outer + inner)
    bosses = [mf.Manifold.cylinder(BOSS_Z[1] - BOSS_Z[0], BOSS_R, circular_segments=64)
              .translate((x, y, BOSS_Z[0])) for x, y in BOSS_XY]
    pilots = [mf.Manifold.cylinder(PILOT_Z[1] - PILOT_Z[0], PILOT_R, circular_segments=32)
              .translate((x, y, PILOT_Z[0])) for x, y in BOSS_XY]
    body = mf.Manifold.batch_boolean([shell] + bosses, mf.OpType.Add)
    return body - mf.Manifold.batch_boolean(pilots, mf.OpType.Add)


# --------------------------------------------------------- iris height field
def collarette_r(phi):
    return 10.4 + 0.55 * np.sin(16 * phi) + 0.2 * np.sin(37 * phi + 1.1) + 0.12 * np.sin(5 * phi + 0.4)


def fibre(R, P, phi0, r0, r1, amp, sigma, wiggle, wavelength, phase, curl, ramp=0.8):
    """Soft radial ridge (Gaussian cross-section) with tapered ends."""
    t = np.clip((R - r0) / (r1 - r0), 0.0, 1.0)
    centre = phi0 + curl * t + wiggle * np.sin(2 * np.pi * (R - r0) / wavelength + phase) / np.maximum(R, 1.0)
    s = R * wrap(P - centre)
    along = smoothstep(r0 - 0.05, r0 + ramp * 0.5, R) * (1 - smoothstep(r1 - ramp, r1, R))
    return amp * along * np.exp(-0.5 * (s / sigma) ** 2)


def iris_relief(R, P):
    """Relief height (mm) above the iris base for polar grid R, P."""
    up = np.zeros_like(R)
    # pupillary zone: fine fibres from the pupil margin to the collarette
    n1 = 60
    for i in range(n1):
        phi = 2 * np.pi * (i + rng.uniform(-0.3, 0.3)) / n1
        up = np.maximum(up, fibre(R, P, phi, R_PUPIL - 0.2, float(collarette_r(phi)) + 0.1,
                                  rng.uniform(0.22, 0.32), rng.uniform(0.14, 0.18),
                                  rng.uniform(0.03, 0.08), rng.uniform(2.0, 3.5),
                                  rng.uniform(0, 2 * np.pi), rng.uniform(-0.03, 0.03), ramp=0.5))
    # crenellated pupillary ruff right at the pupil margin
    ruff = 0.26 * (0.55 + 0.45 * np.cos(72 * P + 0.6 * np.sin(9 * P))) * np.exp(-0.5 * ((R - R_PUPIL - 0.22) / 0.13) ** 2)
    up = np.maximum(up, ruff)
    # collarette: zig-zag crown at about a third of the iris radius
    col = 0.5 * (0.85 + 0.15 * np.sin(23 * P)) * np.exp(-0.5 * ((R - collarette_r(P)) / 0.3) ** 2)
    up = np.maximum(up, col)
    # ciliary zone: main trabeculae
    n2 = 76
    main_phis = []
    for i in range(n2):
        phi = 2 * np.pi * (i + rng.uniform(-0.22, 0.22)) / n2
        main_phis.append(phi)
        up = np.maximum(up, fibre(R, P, phi, float(collarette_r(phi)) - 0.1, R_STEP + 0.3 - rng.uniform(0.0, 1.0),
                                  rng.uniform(0.36, 0.48), rng.uniform(0.19, 0.25),
                                  rng.uniform(0.04, 0.14), rng.uniform(2.5, 5.0),
                                  rng.uniform(0, 2 * np.pi), 0.045 + rng.uniform(-0.02, 0.02)))
    # shorter secondary trabeculae in the outer ciliary zone
    for i in range(n2):
        phi = 2 * np.pi * (i + 0.5 + rng.uniform(-0.25, 0.25)) / n2
        up = np.maximum(up, fibre(R, P, phi, rng.uniform(12.8, 15.4), R_STEP + 0.2 - rng.uniform(0.0, 0.8),
                                  rng.uniform(0.24, 0.34), rng.uniform(0.15, 0.19),
                                  rng.uniform(0.03, 0.1), rng.uniform(2.0, 3.5),
                                  rng.uniform(0, 2 * np.pi), 0.045, ramp=0.6))
    down = np.zeros_like(R)
    # crypts: lacunae between the trabeculae just outside the collarette
    for i in rng.choice(n2, size=28, replace=False):
        phi = wrap((main_phis[i] + main_phis[(i + 1) % n2] + (2 * np.pi if i == n2 - 1 else 0)) / 2)
        rc = rng.uniform(11.4, 14.4)
        sr, ss = rng.uniform(0.45, 0.75), rng.uniform(0.22, 0.3)
        d = np.exp(-0.5 * (((R - rc) / sr) ** 2 + (R * wrap(P - phi) / ss) ** 2))
        down = np.maximum(down, rng.uniform(0.3, 0.4) * d)
    # contraction furrows: broken concentric grooves in the periphery
    for rf in (15.75, 16.95):
        mask = np.zeros_like(P)
        a = rng.uniform(0, 2 * np.pi)
        end = a + 2 * np.pi - 0.3
        while a < end:
            span = min(rng.uniform(1.0, 2.2), end - a)
            centre, half = a + span / 2, span / 2
            mask = np.maximum(mask, 1 - smoothstep(half - 0.25, half, np.abs(wrap(P - centre))))
            a += span + rng.uniform(0.15, 0.4)
        groove = np.exp(-0.5 * ((R - rf - 0.07 * np.sin(11 * P)) / 0.13) ** 2)
        down = np.maximum(down, 0.2 * mask * groove)
    iris_zone = (R >= R_PUPIL) & (R <= R_BLEND)
    return np.where(iris_zone, up - down, 0.0)


def black_iris_body():
    """Black part: everything between the split plane and the iris surface."""
    rings = [(0.0, True)]
    rings += [(r, True) for r in np.linspace(0.5, R_PUPIL, 8)]           # pupil floor
    rings += [(r, False) for r in np.arange(R_PUPIL, R_BLEND, IRIS_DR)]  # pupil wall top .. iris
    rings += [(r, False) for r in np.linspace(R_BLEND, R_LIMBUS, 8)]     # flush limbal ring
    r_arr = np.array([r for r, _ in rings])
    floor = np.array([f for _, f in rings])
    P = np.linspace(0, 2 * np.pi, IRIS_SEGMENTS, endpoint=False)
    RR, PP = np.meshgrid(r_arr, P, indexing="ij")

    base = iris_base(RR)
    headroom = np.maximum(sphere_z(RR) - LID_MARGIN - base, 0.0)   # relief stays inside R40
    top = np.where(RR <= R_BLEND, base + np.minimum(iris_relief(RR, PP), headroom), sphere_z(RR))
    top[floor] = PUPIL_FLOOR
    top[-1, :] = Z_SPLIT                       # rim exactly on the split plane

    # vertices: ring 0 is the centre (single vertex), then rings x segments
    n = IRIS_SEGMENTS
    verts = [np.array([[0.0, 0.0, PUPIL_FLOOR]])]
    for k in range(1, len(r_arr)):
        verts.append(np.column_stack([r_arr[k] * np.cos(P), r_arr[k] * np.sin(P), top[k]]))
    bottom_centre = sum(len(v) for v in verts)
    verts.append(np.array([[0.0, 0.0, Z_SPLIT]]))
    V = np.vstack(verts)

    def ring(k):
        return 1 + (k - 1) * n + np.arange(n)

    tris = []
    j, jn = np.arange(n), (np.arange(n) + 1) % n
    r1 = ring(1)
    tris.append(np.column_stack([np.zeros(n, int), r1[j], r1[jn]]))   # top centre fan
    for k in range(1, len(r_arr) - 1):
        a, b = ring(k), ring(k + 1)
        tris.append(np.column_stack([a[j], b[j], b[jn]]))
        tris.append(np.column_stack([a[j], b[jn], a[jn]]))
    rim = ring(len(r_arr) - 1)
    tris.append(np.column_stack([np.full(n, bottom_centre), rim[jn], rim[j]]))  # bottom fan
    F = np.vstack(tris).astype(np.uint32)

    mesh = mf.Mesh(vert_properties=V.astype(np.float32), tri_verts=F)
    body = mf.Manifold(mesh)
    assert body.status() == mf.Error.NoError, body.status()
    return body, top, r_arr


# ------------------------------------------------------------------- output
def mesh_arrays(m: mf.Manifold):
    mesh = m.to_mesh()
    return np.asarray(mesh.vert_properties)[:, :3].astype(np.float64), np.asarray(mesh.tri_verts)


def write_stl(path: Path, m: mf.Manifold, offset=PLATE_OFFSET, name="RoboEye"):
    v, f = mesh_arrays(m)
    v = v + offset
    tri = v[f]
    nrm = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    nrm /= np.maximum(np.linalg.norm(nrm, axis=1, keepdims=True), 1e-12)
    data = np.zeros(len(f), dtype=[("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")])
    data["n"], data["v"] = nrm, tri
    header = f"{name} realistic eye, mm, plate-03 placement".encode()[:80].ljust(80, b" ")
    with open(path, "wb") as fh:
        fh.write(header)
        fh.write(struct.pack("<I", len(f)))
        fh.write(data.tobytes())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    shell = white_shell_untrimmed()
    white = shell.trim_by_plane((0, 0, -1), -Z_SPLIT)          # keep z <= Z_SPLIT
    black, top, r_arr = black_iris_body()
    # No iris/pupil floor may come closer than MIN_BLACK to the split plane
    # (otherwise white could show inside a recess). Only the flush sphere band
    # at the very rim legitimately runs down to the plane.
    allowed = np.minimum(sphere_z(r_arr), MIN_BLACK)[:, None]
    assert np.all(top >= allowed - 1e-9), float((top - allowed).min())

    black = black.simplify(SIMPLIFY_TOL)
    # Re-check on the final mesh: every vertex between the split plane and
    # MIN_BLACK must lie on the R40 sphere (flush limbal band, no recess).
    bv, _ = mesh_arrays(black)
    in_slab = (bv[:, 2] > Z_SPLIT + 1e-5) & (bv[:, 2] < MIN_BLACK - 1e-5)
    assert np.all(np.abs(np.linalg.norm(bv[in_slab], axis=1) - R_OUT) < 0.01)
    assert bv[:, 2].min() >= Z_SPLIT - 1e-5

    complete = white + black
    assert len(complete.decompose()) == 1
    # Nothing may stick out of the R40 sphere (lid clearance unchanged).
    v, _ = mesh_arrays(complete)
    max_radius = float(np.linalg.norm(v, axis=1).max())
    assert max_radius <= R_OUT + 1e-4, max_radius

    files = {
        "realisticEye_weiss.stl": white,
        "realisticEye_schwarz.stl": black,
        "realisticEye_komplett.stl": complete,
    }
    for name, m in files.items():
        write_stl(OUT / name, m)

    iris_mask = (r_arr > R_PUPIL) & (r_arr < R_BLEND)
    info = {
        "units": "mm",
        "placement": "same as cad/printPlate03White.kcl (centre X/Y 128, rear rim on Z 0, front up)",
        "colour_change_plate_z_mm": round(Z_SPLIT - REAR_PLANE, 3),
        "visible_black_diameter_mm": round(2 * R_LIMBUS, 2),
        "iris_recess_diameter_mm": round(2 * R_BLEND, 2),
        "pupil_diameter_mm": round(2 * R_PUPIL, 2),
        "pupil_depth_below_sphere_mm": round(float(sphere_z(R_PUPIL)) - PUPIL_FLOOR, 2),
        "lowest_iris_floor_above_split_mm": round(float(top[iris_mask].min()) - Z_SPLIT, 3),
        "pupil_floor_above_split_mm": round(PUPIL_FLOOR - Z_SPLIT, 3),
        "max_radius_from_eye_centre_mm": round(max_radius, 4),
        "volumes_mm3": {k: round(m.volume(), 1) for k, m in files.items()},
        "triangles": {k: m.num_tri() for k, m in files.items()},
        "genus": {k: m.genus() for k, m in files.items()},
    }
    (OUT / "build_info.json").write_text(json.dumps(info, indent=2) + "\n")
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main()
