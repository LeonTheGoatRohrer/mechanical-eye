# Bewegungsstudie – Auge und Lider

`mechanismMotionStudy.kcl` ist eine separate, manuell verstellbare CAD-Bewegungsstudie der Druckteile von Platte 1 und 2. **Sie ist keine automatisch abspielbare Animation und keine Video- oder GIF-Datei.** Die vorhandene Montage und die Gesamtbaugruppe bleiben unverändert.

## So durchläufst du die Bewegung
In `mechanismMotionStudy.kcl` oben den Wert von `motionPhase` ändern und das Modell neu berechnen lassen. Für eine feinere Abfolge Zwischenwerte verwenden. Nur Werte zwischen `0_` und `1_` verwenden. Beispiel:

```kcl
motionPhase = 0.0625_
```

| Phase | Gezeigte Stellung |
|---:|---|
| `0_` | Ausgangsstellung, Lider offen |
| `0.0625_` | Blick seitlich, Gier +20° |
| `0.125_` | Mitte |
| `0.1875_` | Blick zur anderen Seite, Gier −20° |
| `0.3125_` | Nick +12° |
| `0.4375_` | Nick −12° |
| `0.5625_` | Lider etwa in der Zwischenstellung, Blink-Eingang 17° |
| `0.625_` | Lider geschlossen, Blink-Eingang 34° |
| `0.75_` | Mitte, Lider offen |
| `0.8125_` | Kombinierter Blick +15°/+8°, Blink-Eingang 17° |
| `0.875_` | Mitte, Blink-Eingang 34° |
| `1_` | Wieder Ausgangsstellung |

## Was sich bewegt
- **Ocker:** Giergestänge und Gieradapter drehen die violette Gabel seitlich um die senkrechte Achse.
- **Grün:** Nickgestänge und Nickadapter kippen den grünlichen Augenträger um die mitgierende Querachse. Der erforderliche Nickservo-Winkel wird aus beiden Blickwinkeln berechnet.
- **Rosa Kurbel, rötliches und goldenes Gestänge:** Ein gemeinsamer Blink-Antrieb bewegt beide Lider über ihre jeweiligen Naben. Für diese Details das Modell von der rechten Seite betrachten.
- **Blaugrau:** Ständer und Grundplatte bleiben ortsfest. Die gelbe Pupille markiert die Blickrichtung; die weiße Schale von Platte 3 fehlt in dieser Ansicht.

Die Farben sind nur eine Ansichtshilfe; die Druckteile sind laut Druckplan schwarz. Servo-Gehäuse, Hörner, Achsen und Schrauben sind nicht dargestellt, deshalb erscheinen Teile ohne reale Halterung. Die gezeigten Winkel sind CAD-Beispiele, keine freigegebenen Servo-Endlagen oder Pulsbreiten. Die Studie berechnet Stellungen, aber keine Kräfte, Kontakte oder reale Geschwindigkeit. Freigängigkeit und Endlagen am echten Aufbau stromlos prüfen.

Neutralstellung, Gier +20°, Nick +12°, Blink-Eingang 34° und die kombinierte Stellung bei Phase 0,8125 wurden separat ausgeführt und visuell betrachtet. Das ist keine vollständige Kollisions- oder Funktionsprüfung; importierte Modulskizzen werden im zentralen Constraint-Bericht nicht vollständig erfasst.
