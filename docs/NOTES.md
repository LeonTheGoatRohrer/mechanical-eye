# Animatronisches Auge – stationäre Servos, innere Blicklagerung

## Aktueller CAD-Stand
`main.kcl` ist die vollständig zusammengesetzte Baugruppe, neutral und mit offenen Lidern. Genau zwei HS-325HB-Referenzen und eine XT-Referenz sind eingebaut. Alle Servogehäuse, Tischteile und Lidaufnahmen bleiben beim Blickwechsel ortsfest. Die früher entfernte Frontwand und ihre beiden Pfosten bleiben entfernt. Ihre alten Quelldateien werden nur als Bestand aufbewahrt.

**Entwicklungsprototyp, keine Fertigungs-/Funktionsfreigabe.** Die CAD-Ausführung und beschränkte analytische Prüfungen sind erfolgt; vollständige Kontakt-, Last- und reale Funktionstests nicht. Alte Phase-A-Unterlagen, Druckplatten und Exporte sind keine Unterlagen des aktuellen Gesamtauges.

## Zwischenstand Druckplatten 1 und 2
`assemblyPrintPlates01And02.kcl` zeigt ausschließlich die 55 schwarzen Druckteile aus `DRUCKTEILE.csv` in den vorhandenen Einbaulagen. `printedGazeJoint.kcl` gruppiert je eine Druckkugel mit zwei gedruckten Distanzstücken ohne Schraube. Darstellung in Kontrastfarben; tatsächliche Druckfarbe laut Druckplan schwarz. Servos, Horn, Schrauben, Achsen und die weiße Schale fehlen bewusst; Pupille und weitere Teile sind daher nur lageorientiert und nicht selbsthaltend. Hinweise und Reihenfolge: `MONTAGE_PLATTE_01_02.md`. Die Gesamtbaugruppe und Druckplatten wurden dafür nicht verändert. CAD-Ausführung und Ansichten erfolgreich; die 14 erfassten Skizzen sind voll bestimmt, importierte Modulskizzen sind im Bericht nicht vollständig erfasst. Kein realer Passungs- oder Montagenachweis.

## Manuelle Bewegungsstudie
`mechanismMotionStudy.kcl` zeigt die Druckteile der Platten 1 und 2 mit unabhängig vom Gesamtmodell vorgegebener manueller `motionPhase` (0–1): Gieren, Nicken, Blinzeln und Kombination. `BEWEGUNGSSTUDIE.md` enthält konkrete Stellungen und die Farblegende. Es ist keine selbstablaufende Animation/Filmdatei. Neutral-, Einzelachsen-, Schließ- und eine kombinierte Stellung wurden ausgeführt und visuell betrachtet; keine vollständige Kontakt- oder Dynamikprüfung. Die 14 erfassten Skizzen sind voll bestimmt; importierte Skizzen sind im Bericht nicht vollständig enthalten.

## Bewegungsprinzip und Dateien
- `gazeAssembly.kcl`: separate Teile, feste Servoaufnahmen und Platzierung der inneren Blickmechanik.
- `innerYawFork.kcl`: innere Giergabel, strukturell auf einer 6-mm-Schulterachse mit Anlaufscheiben gelagert; kein tragender Servoabtrieb.
- `eyeCarrier.kcl`: Nickträger auf zwei koaxialen 4-mm-Schulterzapfen. Beide Blickachsen schneiden sich im Kugelzentrum (0,0,145 mm). Der Augenträger sitzt vor der Gabel, damit er beim Nicken nicht ihre Wangen durchdringt.
- `eyeFront.kcl`: weiße, hinten offene Ø80-mm-Kugelschale, vier innere Blindloch-Befestigungsbosse ohne Durchbrüche/Senkungen auf der sichtbaren Außenfläche, vorhandene getrennte schwarze Pupille. Der bisherige hintere Kugelhalbkörper ist nicht mehr eingebaut.
- `yawSocketRod.kcl` und `pitchSocketRod.kcl`: starre, zweiteilige Kugelpfannen-Gestänge, Mittellängen 75 mm bzw. sqrt(5693) mm. Vier auswechselbare Kugeln, geschraubte Pfannenhälften und konische Distanzstücke erlauben räumliches Schwenken statt erzwungener Gestängebiegung.
- `gazeKinematics.kcl`: exakte skalare Gestängeschließung. Der Nickservo-Winkel hängt von **beiden** Blickwinkeln ab. In der späteren Steuerung nicht einfach Nickservo = Nickwinkel setzen.
- `blinkKinematics.kcl`: vorhandene gekoppelte Zwei-Gestänge-Lidmechanik. Beide Lider bewegen sich nur mit `blinkInput`, nicht mit Blickwinkeln.

| Bewegte Gruppe | Gelenk / Achse | Vorläufiger Prüfbereich |
|---|---|---|
| Innere Giergabel | Drehgelenk um ortsfeste Z-Achse durch Kugelzentrum | −25…+25° |
| Augenträger, Kugel, Pupille | Drehgelenk um mitgierende X-Achse durch dasselbe Zentrum | −15…+15° |
| Ober- und Unterlid | getrennte Drehgelenke um ortsfeste X-Achse; gemeinsame XT-Kopplung | Blinkeingang 0…34° |
| Blickgestänge | Kugelgelenke an beiden Enden | räumlich; keine Biegefreiheit vorausgesetzt |

Damit drei angetriebene Bewegungskoordinaten; kein unabhängiger Rollfreiheitsgrad des Augapfels. Positive Nickrotation um X blickt in dieser Koordinatenkonvention nach unten (Front ist −Y). Kugelgelenke können passive Eigenrotation des jeweiligen Gestänges zulassen; das ist keine zusätzliche angetriebene Augenachse.

## Bedienparameter und Spiel
`assemblyParameters.kcl`: `gazeYaw`, `gazePitch`, `blinkInput`. Standard 0/0/0. `sectionReview=true` macht Kugel und Lider für die Innenansicht transparent, ohne Teile zu versetzen. Normalzustand false.
- `jointDiametralGap=0.3 mm`: **diametrales** Kugelpfannenspiel, entsprechend 0,15 mm radial.
- `shellGapRadial=2.6 mm`: **radialer** Abstand ideale weiße R40-Kugel zur oberen Lidschale Ri42,6.
- `lidGapRadial=1.2 mm`: **radialer** Abstand zwischen oberer Außenfläche und unterer Innenfläche.
- Lidwand 2 mm. Breitere Lidschalen decken nach Entfernung der Frontwand die gesamte Kugelbreite ab.
- Die 4-/6-mm-Achsdurchgänge haben nominal 0,3 mm diametrales Spiel. Passungswerte sind Testansätze, keine garantierten FDM-Passungen.

0,4-mm-Düse angenommen, Filament offen. Neue Teile besitzen noch keinen vollständigen Slicer-/Plattennachweis. Wiederholte Profilfamilien liegen in Funktionen: parametrisch, aber ihre internen Skizzen sind nicht per Punkt-und-Klick editierbar.

## Spätere Kamera
Vorläufiger freier Kamerakörper-Bauraum 22 × 20 × 16 mm im mitbewegten Augenträger, Kameraablage mit zwei M2-Löchern im 16-mm-Raster. Keine konkrete Kamera oder Linse ist eingepasst. Das vorhandene Pupillen-Stemloch ist **keine freigegebene Kameraöffnung**.

Kabel soll aus der rückwärtigen offenen Kugel in einer freien Serviceschlaufe zur erhöhten, ortsfesten Kabelklemme geführt werden; nicht zwischen Kugel und Lid und nicht straff durch die Gierachse. Kein reales Kabelvolumen und keine geprüfte Biegeradius-/Kollisionshülle vorhanden. Erst Kameragehäuse, Objektiv, Stecker, Masse, Kabeldurchmesser und Mindestbiegeradius festlegen, dann bewegungsabhängig auslegen.

## Hardwaredaten und offene Schnittstellen
HS-325HB: Herstellerzeichnung als Grundlage der bestehenden Aufnahme (40×20×36,5 mm, Laschenraster 47,8×10,2 mm, Achsversatz 10 mm längs zur Gehäusemitte). Herstellerblatt: 4,8/6 V, 43 g; 0,19/0,15 s pro 60° **Leerlauf**; 3,0/3,7 kgf·cm **Stillstand**, kein zulässiges Dauermoment; nominell 40° je Seite bei ±400 µs um 1500 µs. In dieser Bearbeitung gelesenes Herstellerblatt:
```text
https://hitecrcd.co.jp/material/spec_sheet/servo/33325.pdf
```
Die Servo-Horngeometrien bleiben ausdrücklich unbestätigte Referenzen (insbesondere Lochradius 9 mm und Dicke 2,5 mm). Originalhörner werden verschraubt, keine gedruckte Verzahnung. Zentralschrauben sind nominale Platzhalter und müssen zur realen Abtriebswelle passen.

XT-Gehäuse-/Hornmaße, Stellbereich, Drehmoment und Geschwindigkeit weiterhin unbekannt. Die vorhandene XT-Aufnahme wurde nicht anhand erfundener Herstellerdaten freigegeben. Keine belastbare Blinzelzeit.

Vorhandene Lager weiterhin Ø22 außen / laut Nutzer Ø9 innen, Breite und Anzahl offen; **nicht als 608 behandelt und in dieser inneren Gabel nicht eingesetzt**. Schulterachsen und Muttern sind Kaufteil-Referenzen; reale Verfügbarkeit, Gewinde und Schulterlängen bestätigen.

## Vorläufige Montage-/Kalibrierreihenfolge
1. Passungen und Kugelpfanne einzeln testen; Achsen müssen nach Anziehen ihrer Schulterbefestigung frei bleiben. Tatsächliche Servo-/Hornmaße aufnehmen.
2. Stationäre Ständer auf Grundplatte verschrauben; Hitecs in ihren Aufnahmen befestigen. Gierlager, Anlaufscheiben und innere Gabel montieren.
3. Weiße Schale zunächst am unveränderten Augenträger von hinten befestigen; erst danach in die Gabel einsetzen. Vier gewindeformende Kunststoffschrauben nominal 2 × 8 mm statt bisheriger langer Durchgangsschrauben und Muttern vorsehen. 4 mm Trägerdicke, 4 mm Eingriff, Blindloch Ø1.7 × 5 mm; 1 mm nomineller Abstand zwischen Schraubenspitze und Lochboden. Pilotmaß ist ein Testansatz und muss mit tatsächlichem Schraubentyp/Filament geprüft werden, nicht als bestätigte Passung behandeln. Nicht durchbohren oder längere Schrauben einsetzen. Pupille unverändert von innen sichern; Kameramodul gegebenenfalls vorher montieren.

Die bereits gedruckte Platte 1 und alle Druckteile von Platte 2 bleiben unverändert. Für die glatte Vorderseite ausschließlich den neu exportierten Stand von printPlate03White.stl verwenden. Schale und Baugruppen erfolgreich ausgeführt und visuell geprüft; kein neuer Slicer-/Festigkeitsnachweis.
4. Servos ohne angeschlossene Gestänge elektrisch neutralisieren. Originalhörner und Adapter anschrauben. Kugeln mit Distanzstücken an Hebeln befestigen, Pfannenhälften um die Kugeln verschrauben.
5. Bestehende ortsfeste Lidachse, beide Lidnaben, Abstandshülsen und XT-Gestänge montieren; keine Lidbewegung durch Festziehen der Achsmutter blockieren.
6. Zuerst manuell und ohne Strom auf Freigängigkeit prüfen, dann kleine Einzelwinkel, anschließend kombinierte Winkel mit berechnetem Nickservo-Winkel. Erst danach langsam blinzeln und Kabelschlaufe ergänzen. Endstellungen nicht gegen blockierende Teile kalibrieren.

Weitere offene Prüfungen siehe `PRUEFBERICHT.md` und `CHECKLIST.md`.
