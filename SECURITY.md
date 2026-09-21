# Security Policy

Die ausführliche technische Richtlinie liegt in [references/SECURITY_POLICY.md](references/SECURITY_POLICY.md).

## Sicherheitslücken melden

Bitte keine verwertbaren Exploit-Details, Secrets oder personenbezogenen Daten in öffentlichen Issues veröffentlichen.

Bevorzugter Meldeweg:

1. GitHub Private Vulnerability Reporting / Security Advisory verwenden, sofern für das Repository aktiviert.
2. Falls dieser Kanal nicht verfügbar ist, ein öffentliches Issue nur mit dem Hinweis eröffnen, dass ein privater Kontaktkanal für einen Sicherheitsbericht benötigt wird. Keine technischen Exploit-Details anhängen.

## Scope

Sicherheitsrelevant sind insbesondere:

* Prompt Injection und Instruction Override
* Credential- oder Secret-Exposure
* unsichere Codeausführung
* Supply-Chain- und Dependency-Risiken
* gefährliche Tool-/Connector-Berechtigungen
* Pfad-Traversal oder unerwarteter Netzwerk-Egress
* manipulierbare Provenienz oder Registry-Metadaten

## Release Gate

Kein neuer oder geänderter Skill soll freigegeben werden, wenn ein CRITICAL- oder HIGH-Befund des Security-Auditors offen ist.
