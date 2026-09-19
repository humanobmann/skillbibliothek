# Reaktion auf Zustellbarkeitsvorfälle

## Auslöser

* SMTP-Code `5.7.x`, Policy- oder Spamblock
* ungewöhnlich viele Nachrichten in kurzer Zeit
* serielle Betreffzeilen oder identische Inhalte
* `winmail.dat` oder `application/ms-tnef`
* unbekannte Empfängerzahl oder Versand außerhalb des Ledgers
* unerwartete Beschwerden, Opt-outs oder Kontowarnungen

## Sofortmaßnahmen

1. Alle neuen Erstkontakte über alle Kanäle pausieren.
2. Keine blockierte Nachricht unverändert erneut senden.
3. Keine Ersatzadresse derselben Organisation verwenden.
4. Zeitraum, Kanal, Empfänger, Betreff, Anlagen, SMTP-Diagnosen und Antwortstatus sichern.
5. Bounces nach Diagnose klassifizieren, nicht nach Gefühl.
6. CRM und Mailbox abgleichen. Fehlende Versandereignisse als Datenlücke markieren.
7. Serienmuster, Tagesmenge, Zehn-Minuten-Spitzen und TNEF prüfen.

## Ursachenprüfung

* Absender und Reply-to korrekt
* Konto nicht kompromittiert oder eingeschränkt
* SPF, DKIM und DMARC soweit für den Dienst prüfbar
* Klartext- und HTML-Version sauber
* keine TNEF-Anlage
* Linkzahl und Linkziel plausibel
* Anlagengröße und Assetversion
* Betreff und Inhalt individuell
* Empfängerquelle und thematische Passung

## Wiederanlaufkriterien

Zeitablauf allein reicht nicht. Wiederanlauf erst, wenn:

1. Umfang und Ursache dokumentiert sind
2. alle betroffenen Empfänger im Ledger stehen
3. Spamblocks nicht als ungültige Adressen entsorgt wurden
4. Versandformat ohne TNEF getestet ist
5. Absenderidentität und Kontostatus bestätigt sind
6. neue Pilotwelle aus höchstens drei besonders passenden Empfängern vollständig geprüft ist
7. Vorschau und ausdrückliche Versandfreigabe vorliegen

Nach der Pilotwelle mindestens drei Werktage Ergebnisse beobachten. Erst nach drei sauberen Pilotwellen auf höchstens fünf bis acht Empfänger erweitern. Automatische Skalierung bleibt ausgeschlossen.

## Abschlussbericht

* Zeitraum und betroffene Kanäle
* Nachrichten und eindeutige Empfänger
* Versandspitzen
* Bounceklassen
* Antworten und Opt-outs
* wahrscheinliche Ursachen
* technische und redaktionelle Änderungen
* Wiederanlaufdatum und Grenzwerte
* offenes Restrisiko
