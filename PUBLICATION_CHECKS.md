# Publication verification — 2026-11-02

## Scope and provenance

The existing `Auge1.stl` has been retained unchanged. This update adds the available RoboEye KCL project, its documentation, the complete existing assembly export, all three print-plate meshes and static previews rendered from those meshes.

- `exports/assembly/RoboEye.obj`: unchanged local OBJ export dated 2026-10-31.
- `exports/assembly/main.stl`: binary STL conversion of every triangle in that OBJ. No remeshing, simplification, union or removal of assembly components was performed. Contains hardware references and intersecting installed components; do not print as one object.
- `exports/print-plates/printPlate01Black.stl`: binary conversion of the existing `printPlate01Black.stl` export dated 2026-10-13.
- `exports/print-plates/printPlate02Black.stl`: binary conversion of the later existing `printPlate02Black (1).stl` export dated 2026-10-15, rather than the earlier 2026-10-13 file.
- `exports/print-plates/printPlate03White.stl`: extracted from OBJ object `Unnamed-182`. Identification was checked against the shell bounds, centre height 145 mm and all four radius-0.85-mm blind pilot bores at X ±28 mm / Z 137 and 153 mm. The bore vertices run from assembly Y −23 to −18 mm, matching `cad/eyeFront.kcl`. Placement exactly follows `cad/printPlate03White.kcl`: undo the assembly translation, rotate −90° around X, translate by (128, 128, −7) mm. Equivalently: `(x, y, z) → (x + 128, z − 17, −y − 7)`. Triangle connectivity and shape were retained.

All STL files use 32-bit coordinates as required by binary STL; conversion error was checked to remain below 0.00001 mm per coordinate. Coordinates are finite and binary triangle counts match file lengths. Units are millimetres by project convention; STL does not encode units or colours.

## Mesh checks

| Export | Triangles | Connected components | Dimensions X × Y × Z (mm) | Boundary edges | Edges with >2 incident faces |
|---|---:|---:|---|---:|---:|
| Assembly | 302,596 | 237 | 268.5 × 165 × 201 | 0 | 2,354 |
| Plate 01 | 6,574 | 6 | 245 × 242 × 175 | 0 | 0 |
| Plate 02 | 82,036 | 49 | 245.5 × 251 × 47.79943 | 0 | 0 |
| Plate 03 | 16,302 | 1 | 78.76547 × 78.76547 × 32.87179 | 0 | 0 |

All four exports contain zero zero-area triangles. Edge and component checks merge vertices rounded to 0.00001 mm. Assembly components touching or sharing geometry can produce edges with more than two incident faces; this assembly is an inspection export, not a single printable solid. The three plate meshes have the expected 6 + 49 + 1 connected components, within 0–256 mm in X/Y and on Z = 0 to float precision. Four preview PNGs were visually inspected.

Source checks: every local `.kcl` import in the published `cad/` directory resolves. All supplied KCL files were copied without edits. The publication's `cad/project.toml` retains the title and entry point but omits local cloud metadata. Generated `thumbnail.png` and `._meta` files are excluded. No KCL engine reevaluation was performed, so the existing plate 01/02 exports are not certified as regenerated from the supplied KCL snapshot.

Exact output bounds, sizes, SHA-256 hashes and source-export SHA-256 hashes are recorded in [exports/verification.json](exports/verification.json). These are structural and provenance checks, not a slicer, collision, printability, physical-fit or functional certification. Existing limitations in [docs/DRUCKPLAN.md](docs/DRUCKPLAN.md) and [docs/NOTES.md](docs/NOTES.md) remain applicable.

## Original publication verification — 2026-10-29

STL parsed successfully: 9,624 triangles; all vertex coordinates finite; triangle/vertex counts consistent. Bounds: X 14–234, Y 38–182, Z approximately 0–24 in file units. This is a structural file check, not a watertightness, slicer, printability or physical fit certification. Ownership and public release were explicitly confirmed by the user on 2026-10-29.

The final upload status and actual remote commit are verified separately after pushing. A successful source upload does not imply that skipped physical, external-service or production checks passed.
