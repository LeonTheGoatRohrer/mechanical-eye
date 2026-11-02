# Montage und Kalibrierung – Teilstand A

Nur die beiden Hitec-Aufnahmemodule lassen sich nach diesem Stand zusammenbauen. Das Auge selbst besitzt noch keine vollständigen Befestigungs- und Antriebsschnittstellen. Schrauben sind in der Stückliste vorgeschlagen, aber nicht als CAD-Körper dargestellt.

## Nummerierte Montage der Module
1. Coupon/Testzapfen mit vorgesehenem Material drucken. Lager nur von Hand in die Prüflöcher einsetzen, nicht hineinpressen. Verwendbare diametrale Zugaben dokumentieren; ID9 und Breite nachmessen.
2. Eine Hitec-Adapterplatte prüfen: Gehäuse muss durch40,8×20,8 passen, vier Laschenöffnungen müssen zum47,8×10,2-Raster passen. Tüllen oder abweichende Horn-/Kabelgeometrie jetzt berücksichtigen.
3. Vier M3x40-Schrauben mit Scheiben durch die Grundplatte stecken; vier24-mm-Hülsen aufschieben. Gewählter Kopf unten muss zum späteren Ständer passen, der noch nicht konstruiert ist.
4. Servo zunächst bei freiem Zugang über seine vorhandenen Laschen mit Adapterplatte verschrauben: Vorschlag vier M3x12, Scheiben und Muttern. Nicht übermäßig festziehen; Kunststofflaschen nicht quetschen. Kein Horn gegen das Getriebe verdrehen.
5. Adapter-/Servomodul auf die vier Hülsen setzen, obere Scheiben/Muttern anbringen. Werkzeugzugang an allen vier Ecken und Kabelausgang am tatsächlichen Servo kontrollieren. Kabel liegt weder unter einer Hülse noch unter dem Gehäuse eingeklemmt.
6. Zweites Modul identisch montieren. Die beiden Module sind noch nicht mit einem Tischständer verbunden. Kein angetriebenes Auge anschließen.

Explosionsdarstellung: In `main.kcl` stellt `explodedOffset=18mm` Adapter und Servoreferenz auseinander;0 mm ist montiert. Eine solche Explosionsansicht wurde gerendert. Sie ersetzt keine Explosion der noch fehlenden Gesamtmechanik.

## Vorgesehene sichere Inbetriebnahme der späteren Mechanik
Noch keine freigegebenen Software-Endpunkte und keine ausgelegten Schutzanschläge.
1. Erst nach vollständiger Lager-/Gestänge- und Kollisionsprüfung: stromlos von Hand alle Bewegungsräume prüfen, zunächst ohne Servohörner/Gestänge.
2. Servos einzeln, mechanisch entkoppelt, mit passender Versorgung und Strombegrenzung prüfen. Für Hitec nennt das Herstellerblatt1500 µs Neutral; XT-Neutral und zulässige Pulse erst identifizieren. Keine pauschalen500…2500 µs oder180° verwenden.
3. Originalhörner in Neutralstellung montieren und markieren. Gedruckte Adapter erst nach Lochbildprüfung anschrauben; keine gedruckte Ersatzverzahnung.
4. Auge neutral ausrichten, Gestänge kraftfrei auf Länge einstellen. Zuerst kleine Einzelachsenbewegungen, dann schrittweise vergrößern. Ziel±30°/±20° ist noch kein erlaubter Betriebsbereich.
5. Lidservo getrennt: erst Teilhub, dann schrittweise optischen Abschluss einstellen. Schalen dürfen weder auf dem Auge reiben noch gegeneinander drücken. Danach alle Kombinationen aus Blick und Lidstellung prüfen.
6. Freigegebene Softwaregrenzen mit Abstand zu den späteren mechanischen Schutzanschlägen setzen; langsam beginnen, Strom/Erwärmung/Spiel beobachten. Bei Blockade sofort stoppen, nicht wiederholt gegen Anschläge fahren.
7. Erst nach dokumentierter Kollisionsfreiheit, ausreichendem Drehmoment, sicherer Kabelbewegung und Kippsicherheit Bewegungsrampen/Blinzeltempo erhöhen.

Keine dieser realen Prüfungen wurde hier durchgeführt.
