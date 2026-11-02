# Montagezwischenstand – Druckplatten 1 und 2

## Ansicht und Umfang
`assemblyPrintPlates01And02.kcl` zeigt die 6 Druckteile von Platte 1 und die 49 Druckteile von Platte 2 in den vorgesehenen Einbaulagen der bestehenden Gesamtbaugruppe. Die Farben in dieser Ansicht dienen nur der Unterscheidung; der Druckplan sieht schwarze Teile vor. Die vollständige Baugruppe `main.kcl` und die Druckplatten bleiben unverändert.

Die weiße Augenschale von Platte 3, Servos, Originalhörner, Schrauben, Muttern, Metallachsen und Metallscheiben sind **nicht** dargestellt. Ohne diese Kaufteile halten mehrere Teile nicht in der gezeigten Lage. Die Pupille ist nur an ihrer späteren Position dargestellt und kann ohne die weiße Schale nicht befestigt werden. Die Darstellung ist ein Orientierungsmodell, kein Nachweis der realen Montage oder Passung.

## Vorgehen
1. Druckteile anhand `DRUCKTEILE.csv` sortieren. Bohrungen, Zapfen und Kugelpfannen zunächst einzeln auf Passung prüfen; keine Gewalt oder Presspassung voraussetzen.
2. Die vier Füße unter die Grundplatte setzen. Die fünf Ständer aus Platte 1 anhand der Bohrungen ausrichten und mit passenden, separat beschafften Schrauben befestigen.
3. Zentrale Blicklagerung, Giergabel und Anlaufscheiben zuordnen. Die Nick-Anlaufscheiben sind 2 mm lang, die Gier-Anlaufscheiben 1 mm. Hierfür werden passende Achsen und Befestigungen benötigt. Den Augenträger ohne weiße Schale höchstens provisorisch einsetzen: Laut aktuellem Entwurf wird die Schale vor dem endgültigen Einsetzen des Trägers von hinten befestigt.
4. Die beiden Hitec-Montageplatten und vier 3-mm-Nick-Montagedistanzen an den zugehörigen Ständern zuordnen. Die Adapter und XT-Klemmbügel benötigen die tatsächlichen Servos, Originalhörner und Befestigungen; ohne diese nur bereitlegen. Servos vor dem Anschluss der Gestänge neutralisieren und die realen Horn- und Gehäusemaße prüfen.
5. Ober- und Unterlid mit ihren jeweiligen Naben, der Lidsäule und der getrennt beschafften Achse zusammenfügen. Die drei gedruckten Liddistanzen der Reihe nach vorne, mittig und hinten zuordnen: 1,8 / 4,3 / 1,3 mm. Die 13-mm-Distanz gehört an den Eingang des Oberlidgestänges. Axialspiel und freie Bewegung nach dem Festziehen prüfen.
6. Je zwei Hälften für Gier- und Nickgestänge zuordnen. Zu jedem der vier Kugelgelenke gehören eine Kugel und zwei konische Distanzstücke. Die Pfannenhälften und Kugeln benötigen passende Schrauben; Antriebsadapter erst an geprüften Originalhörnern befestigen.
7. Kabelklemme befestigen. Pupille für die weiße Schale aufbewahren. Die weiße Schale später nach `NOTES.md` von hinten am Augenträger befestigen; Pilot und Schraubenlänge vorab prüfen.

Die vorhandene `BOM.csv` und `MONTAGE.md` beschreiben einen historischen Teilstand und sind keine aktuelle Gesamtstückliste. Reale Schraubenlängen, Achsen, Servoschnittstellen und Passungen vor der Montage prüfen. Erst stromlos von Hand auf Freigängigkeit testen; das Modell ersetzt keine Kollisions- oder Funktionsprüfung.
