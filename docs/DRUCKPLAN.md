# Druckplan – aktuelles Gesamtauge

## Dateien und Umfang
| CAD-Datei / gleichnamiges STL | Farbe | Anzahl |
|---|---|---:|
| printPlate01Black.kcl | Schwarz: Grundplatte und fünf stationäre Halter | 6 |
| printPlate02Black.kcl | Schwarz: Lider, Mechanik, Pupille und Kleinteile | 49 |
| printPlate03White.kcl | Weiß: aktuelle offene Augenschale | 1 |

Gesamt: **56 Druckteile**, Mengenabgleich mit main.kcl und gazeAssembly.kcl. Vollständige Druckstückliste: DRUCKTEILE.csv. Platte 1 und sämtliche Druckteile auf Platte 2 bleiben auch nach der Umstellung auf die glatte Augenfront unverändert. Platte 3 enthält jetzt eine geänderte Schale mit vier inneren Blindlöchern statt sichtbarer Durchgangslöcher. Befestigung von hinten mit vorgesehenen Kunststoffschrauben 2 × 8 mm; keine alten 16-mm-Schrauben verwenden. Neuer Pilot Ø1.7 mm muss mit Schraubentyp und Filament getestet werden; Montagehinweise in NOTES.md. Nutzer meldet erfolgreiche Tests; dies ersetzt keinen Slicer-Nachweis dieser Platten.

Drei kompakte, farbgetrennte CAD-Anordnungen für 256 × 256 × 256 mm. Keine mathematisch nachgewiesene Minimalzahl und keine abschließend geprüfte Belegung einschließlich Brims und Supports. Alle drei Dateien wurden ausgeführt, gerendert und als STL exportiert. Das Constraint-Reporting der Platten erfasst nicht sämtliche Skizzen innerhalb importierter Module.

Nicht drucken: Servoreferenzen, Originalhörner, Schrauben, Muttern, Schulterachsen, metallische Unterleg-/Passscheiben einschließlich der 0.1- und 0.5-mm-Scheiben. Diese Kaufteile bleiben für die Montage erforderlich. Nicht enthalten: Testcoupon/Testzapfen, alte Studien, alte Modulgrundplatten/24-mm-Hülsen, entfernte Frontwand/Pfosten und hintere Augenschale. BOM.csv ist weiterhin die historische Phase-A-Liste, NICHT die aktuelle Druckstückliste.

## Vor dem Start im Slicer
- STL in Millimetern importieren; Kontrollmaß Grundplatte 244 × 164 × 6 mm. Nicht skalieren.
- Je STL eine Platte; bei Bedarf in einzelne Objekte zerlegen und Anordnung zunächst beibehalten. Druckreihenfolge nach Schichten, keine ungeprüfte sequenzielle Einzelobjekt-Reihenfolge.
- Tatsächliches Druckerprofil, Material und Düse auswählen. Sperrflächen, Startlinien, Brims sowie Support-Fußabdrücke prüfen. Die Anordnung lässt nicht überall Platz für breite Brims.
- Schichtvorschau zwingend prüfen, insbesondere hohe Halter, Kugeln, Pupille, Augenträger und Schalen. Supports werden ausschließlich im Slicer geplant; im CAD/STL sind keine enthalten.
- Dünne Ränder und kleine Bohrungen müssen echte Werkzeugbahnen erzeugen. Getestete Passungen nicht durch globale Skalierung verändern.

## Geometrisches Screening und Grenzen
FDM-Meshscreening mit +Z-Baurichtung, 0.2-mm-Abtastschichten und 45° zur Bauplatte als Überhang-Heuristik; Material/Düse sowie Mindestwand-, Spalt- und Kontaktflächenanforderungen unbekannt. Keine Haftungs-, Festigkeits-, Druckzeit- oder Filamentverbrauchsfreigabe.

Screening der schwarzen Platten erfolgte vor den letzten XY-Verschiebungen/der Z-Drehung. Danach CAD-Ausführung und STL-Export erfolgreich; das Screening ist kein Nachweis der endgültigen Abstände. Die untersuchten Meshes zeigten keine Integritätswarnungen und keine Bauraumüberschreitung. Überschneidungen/Selbstüberschneidungen sind damit nicht umfassend ausgeschlossen.

- Platte 1: 14 Überhangwarnungen; Inselprüfung über 875 Schichten abgeschlossen. Hohe Halter und Ausleger im Slicer prüfen. Abgetastete Wand-/Spaltwerte sind keine kontinuierlichen Minima.
- Platte 2: 38 Überhangwarnungen. Inselprüfung nur 19 von 239 Schichten, Abbruch wegen ungültiger Schnittkontur. Wand-/Spaltprüfung nur 10000 von 82072 Dreiecken. Kleinste abgetastete Dicke ca. 0.154 mm am Oberlidrand; kein Nachweis der nominellen Gesamtwandstärke. Rand im Slicer besonders prüfen, Originalgeometrie unverändert.
- Historischer Stand Platte 3 VOR der glatten Front: 5 Überhangwarnungen und vier zunächst ungestützte Boss-Inseln bei ca. 11.1 mm Höhe. Inselprüfung über 165 Schichten abgeschlossen. Wand-/Spaltprüfung nur 10000 von 17248 Dreiecken; kleinste abgetastete Dicke ca. 0.161 mm und Spalt ca. 0.083 mm im Befestigungsbereich. Lokale Werte sind tessellierungs-/abtastabhängig und keine Passungsbewertung. Diese Messwerte gelten nicht für die geänderte Schale. Neuer Stand CAD-validiert und als STL exportiert, aber ohne erneutes DFM-Screening; Innenbosse und Schalenüberhänge im Slicer neu prüfen. Weiße Schale NICHT ungeprüft als supportfreien Druck starten.

Kontaktflächen wurden nur insgesamt geometrisch erfasst, nicht als Haftung oder Stabilität jedes Einzelteils bewertet. Herkunftszuordnung importierter Flächen teilweise unaufgelöst. Vollständige Slicerprüfung bleibt offen; zusätzliche Platten können erforderlich werden, wenn die tatsächlichen Support-/Brimflächen nicht passen. Es wurde kein 3MF/Slicerprojekt und kein G-Code erstellt.

## Historische Testplatte
blackPlatePhaseA.kcl bleibt unverändert als alte Testanordnung erhalten. Sie ist für diesen vollständigen Drucksatz nicht erforderlich.
