# Prüfbericht – innere Blicklagerung mit stationären Servos

## Ergebnis und Grenze
Native Einzelteile und montierte Assembly sind ausgeführt. All drei Servogehäuse, äußere Ständer und Lidaufnahmen bleiben bei Blickbewegungen fest. Die Blickgestänge sind über Kugelgelenke verbunden; die räumliche Nick-Gestängelänge wird rechnerisch geschlossen. **Keine vollständige Kollisions-, Dynamik- oder Fertigungsfreigabe. Keine realen Prototypentests.**

## Tatsächlich durchgeführt
- Neue Teile separat validiert; ausgeführte Solver-Skizzen vollständig bestimmt, keine Unter-/Überbestimmung in den erfolgreichen Berichten.
- Abschließende `eyeCarrier.kcl`-Validierung: 10 vollständig bestimmte Skizzeninstanzen; Volumen 8.913,06 mm³.
- Abschließende `eyeFront.kcl`-Validierung: 4 vollständig bestimmte Skizzen; Volumen 14.618,41 mm³. Bohrungen und Schraubensitze sind echte Subtraktionen.
- `gazeAssembly.kcl`: 133 lokale vollständig bestimmte Instanzen; `main.kcl`: 99 lokale Instanzen. Importierte Teilskizzen wurden separat geprüft, diese Zahlen sind nicht die vollständige Gesamtzahl.
- Augenträger nach vorne versetzt und Ecken gekürzt, um zuvor erkannte Überschneidung mit der Giergabel zu beseitigen. Schalenbefestigungen angepasst, Servoaufnahmen versetzt und Kabelklemme über die Gestänge angehoben.
- `gazeMotionChecks.kcl` erfolgreich ausgeführt: **1.581 Positionen**, 1°-Raster für Gier −25…+25° und Nick −15…+15°.

### Was der Rastertest prüft
1. Konstante Nickgestängelänge sqrt(5693) mm, quadrierter normierter Schließfehler <0,00001.
2. Berechneter Nickservo-Winkel innerhalb −35…+35°. Das ist eine bestandene Prüfgrenze, nicht ein ermitteltes exaktes Minimum/Maximum.
3. Betrag der normierten Eingangs-Kreis-Schließgröße <0,85: Abstand zur untersuchten Eingangssingularität.
4. Konservative Winkelgrenzen für die seitliche Kugelgelenkauslenkung unter 38°.
5. Wirksamer Gierhebelarm >10 mm.
6. Vereinfachte Hüllabstände der beiden Blickgestänge zum schmalen zentralen Ständer >2 mm an den untersuchten Schnitten.
7. Analytischer Abstand des nach vorne versetzten Augenträger-Rahmens zur vorderen Gabelkante >3 mm über den getesteten Nickbereich.

Nicht enthalten: vollständige paarweise Solid-Kontaktprüfung aller Teile, vollständige Gelenklast-/Jacobi-Auswertung oder kontinuierlicher Beweis zwischen Rasterpunkten. Die Winkelgrenzen an den Kugelgelenken ersetzen keinen realen Klemm-/Reibungstest.

## Visuelle Prüfung der finalen Geometrie
| Gier | Nick | Blinkeingang | Ansicht |
|---|---|---|---|
|+25°|−15°|17°|transparente Kugel/Lider, Vorder- und Rückseite|
|−25°|+15°|0°|transparente diagonale Mechanikansichten|
|+25°|+15°|34°|transparente Mechanikansichten bei geschlossenen Lidern|
|−25°|−15°|34°|Front deckt weiße Augenöffnung vollständig schwarz ab; Rückseite geprüft|
|0°|0°|0°|abschließend normal zusammengebaut: Dreiviertel, Rückseite, inneres Detail und Front|

Diese Ansichten zeigen ausgewählte Stellungen, keine zeitliche Kontakt-/Dynamiksimulation. Die Gehäuse-/Ständerplatzierungen hängen im Code nicht von Blickwinkeln ab. Die Lidpositionen hängen ausschließlich von der gemeinsamen vorhandenen Blinkkinematik ab, nicht von einer frei gewählten Lidanimation.

Ideale konzentrische Flächen: Kugel R40 zu Oberlid Ri42,6 = 2,6 mm radial; Oberlid Ra44,6 zu Unterlid Ri45,8 = 1,2 mm radial. Diese Abstände gelten nicht pauschal für Schrauben/Bosse, Lagerfehler, Druckverzug oder Kabel. Schalenbreite wurde für die Frontansicht ohne frühere Frontwand vergrößert.

## Antriebe / bewegte Masse
- Gierservo bewegt die innere Gabel über ein 1:1-Gestänge: Prüfbereich ±25°.
- Nickservo muss die gekoppelte Lösung aus `gazeKinematics.kcl` erhalten; alle Rasterpunkte liegen innerhalb ±35°. Direkte unabhängige Winkelzuweisung würde das starre Gestänge verspannen.
- XT-Blinkeingang 0° offen, 17° Zwischenstellung, 34° geschlossen. Das sind CAD-Eingangsstellungen, nicht verifizierte Pulsbreiten des unbekannten XT.
- Nur zwei Einzelteilvolumina neu gemessen, keine vollständige Massen-/Trägheitsauswertung. Aus diesen Werten wird keine garantierte Drehmomentreserve abgeleitet. Reibung der gedruckten Kugelpfannen, Beschleunigung, Kabelkräfte und Kameramasse sind offen.
- HS-325HB-Stillstandswerte sind keine zulässigen Dauerlasten. XT-Kraft und -Geschwindigkeit nicht nachgewiesen, deshalb keine zugesagte Blinzelzeit.

## Nicht durchgeführt / erforderlich
- Vollständige Kollisionsmatrix einschließlich Schraubenköpfen, realen Hörnern, Kabeln und Werkzeugen über den gesamten Bewegungsbereich.
- Alle Blickpositionen kombiniert mit allen Zwischenstellungen des Blinzelns; vollständige kontinuierliche Totpunkt-/Lastprüfung der bestehenden Lidmechanik.
- Drehmoment-, Steifigkeits-, Verschleiß-, Standfestigkeits- und Temperaturtests; keine FEA oder physikalische Bewegungssimulation.
- Kamerakabel-Schlaufe mit realem Mindestbiegeradius und Zugentlastung; reale Kamera-/Objektivpassung.
- Gleit-/Kugelpassungen, Schulterachsen-Verfügbarkeit und Toleranzstapel am gedruckten Prototyp. Schulterachse statt Gewindefläche als laufende Lagerfläche sicherstellen.
- Schutzanschläge, dauerhafte Neutralmarkierungen und längeneinstellbare Kalibrierung der neuen starren Blickstangen weiterentwickeln. Der aktuelle Entwurf benutzt feste, parametrisch veränderbare Stangenlängen.
- Vollständige neue Schwarz-/Weiß-Druckplatten und Slicerprüfung. **Kein Nachweis eines gemeinsamen schwarzen Druckdurchgangs.** Alte Phase-A-Testplatte ist nicht die Gesamtbaugruppe.
- Aktualisierte Gesamt-BOM, vollständige technische Zeichnungen und neue STEP/STL/3MF-Ausgaben sind in dieser Überarbeitung nicht erzeugt.

## Historische Phase A
Das frühere FDM-Screening betraf ausschließlich eine 14-Körper-Testplatte mit Aufnahmen/Passungstests, nicht die jetzige Assembly oder die neuen Kugelgelenke. Seine Ergebnisse sind nicht auf diese Konstruktion übertragbar. Frühere Exporte und übrige Phase-A-Dokumente sind entsprechend nur historische Teil-Lieferungen.
