# Setup Playbook

## Zielbild

Baue eine moderne PowerShell-Admin-Umgebung mit:

- Windows 11 Admin-PC als primärer Arbeitsplatz
- PowerShell 7 als Standard-Shell für neue Arbeit
- Windows PowerShell 5.1 nur für Legacy-/Windows-only-Module
- VS Code + Microsoft PowerShell Extension als Editor
- Git und GitHub-/Azure-DevOps-kompatible Arbeitsweise
- Azure Cloud Shell als browserbasierte, authentifizierte Azure-Notfall- und Mobilumgebung
- SecretManagement/SecretStore oder Azure Key Vault für Geheimnisse
- PSScriptAnalyzer für statische Prüfung

## Windows 11 Admin-PC: Basisinstallation

Empfohlene Reihenfolge:

```powershell
# PowerShell 7 installieren oder aktualisieren
winget install --id Microsoft.PowerShell --source winget
winget upgrade --id Microsoft.PowerShell --source winget

# VS Code installieren
winget install --id Microsoft.VisualStudioCode --source winget

# Git installieren
winget install --id Git.Git --source winget

# Windows Terminal installieren, falls nicht vorhanden
winget install --id Microsoft.WindowsTerminal --source winget
```

Nach der Installation eine neue Shell öffnen und prüfen:

```powershell
pwsh
$PSVersionTable
Get-Command git, code, pwsh
```

## PowerShell-Profil

Verwende ein schlankes CurrentUser-Profil. Keine schweren Cloud-Module automatisch importieren.

```powershell
if (-not (Test-Path -LiteralPath $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
}
code $PROFILE
```

Sinnvolle Inhalte:

```powershell
Set-StrictMode -Version Latest
$PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
$InformationPreference = 'Continue'

function prompt {
    "PS $($ExecutionContext.SessionState.Path.CurrentLocation)> "
}

Set-PSReadLineOption -PredictionSource HistoryAndPlugin -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows
```

Nutze Profilcode konservativ. Wenn Profilfehler Admin-Arbeit blockieren, mit `pwsh -NoProfile` starten.

## VS Code + PowerShell

Installiere mindestens diese Extensions:

```powershell
code --install-extension ms-vscode.PowerShell
code --install-extension ms-vscode.azure-account
code --install-extension ms-azuretools.vscode-azureresourcegroups
code --install-extension eamodio.gitlens
code --install-extension editorconfig.editorconfig
```

Empfohlene VS-Code-Einstellungen für PowerShell-Projekte:

```json
{
  "powershell.powerShellDefaultVersion": "PowerShell (x64)",
  "powershell.scriptAnalysis.enable": true,
  "powershell.codeFormatting.autoCorrectAliases": true,
  "powershell.codeFormatting.useConstantStrings": true,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "editor.formatOnSave": true
}
```

## Git-Standard

```powershell
git config --local user.name "<name>"
git config --local user.email "<email>"
```

Lokale Repository-Konfiguration bevorzugen. Globale Git-Einstellungen nur auf ausdrücklichen Wunsch und nach Prüfung bestehender Werte ändern. Für wiederverwendbare Skript-Repositories `.gitignore`, `.editorconfig`, Projektdokumentation und Tests nach tatsächlichem Bedarf anlegen.

## Modulmanager

Für PowerShell 7 bevorzugt PSResourceGet verwenden, wenn verfügbar. Fallback: PowerShellGet `Install-Module`.

```powershell
Get-Module Microsoft.PowerShell.PSResourceGet -ListAvailable
Get-PSResourceRepository
Find-PSResource PSScriptAnalyzer
```

Fallback:

```powershell
Get-PSRepository
Install-Module -Name PSScriptAnalyzer -Scope CurrentUser -Force
```

## Basismodule

```powershell
# Qualität und Sicherheit
Install-Module -Name PSScriptAnalyzer -Scope CurrentUser -Force
Install-Module -Name Microsoft.PowerShell.SecretManagement -Scope CurrentUser -Force
Install-Module -Name Microsoft.PowerShell.SecretStore -Scope CurrentUser -Force

# Azure und Microsoft 365 nur installieren, wenn diese Zielsysteme wirklich gebraucht werden
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
Install-Module -Name Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force
Install-Module -Name ExchangeOnlineManagement -Scope CurrentUser -Force
Install-Module -Name MicrosoftTeams -Scope CurrentUser -Force
```

Produktionshinweis: Große Rollup-Module wie `Microsoft.Graph` und `Az` sind bequem, aber schwer. Für Automationen nach Möglichkeit nur benötigte Submodule installieren.

## Azure Cloud Shell

Nutze Azure Cloud Shell für schnelle Azure-Administration, wenn lokale Tools fehlen oder ein sauberer, browserbasierter Kontext gewünscht ist. Beachte:

- Sitzung ist temporär und läuft bei Inaktivität ab.
- `$HOME` wird über Azure Files persistiert.
- Azure CLI und Azure PowerShell sind bereits authentifiziert und vorkonfiguriert.
- Keine lokalen Windows-/RSAT-Annahmen treffen.
- Persistente Skripte in Git oder im Cloud-Shell-Home speichern.

Prüfen:

```powershell
$PSVersionTable
Get-Module Az.Accounts -ListAvailable
Get-AzContext
```

## Windows-only und Legacy

Nutze Windows PowerShell 5.1 nur, wenn ein Modul nicht sauber in PowerShell 7 funktioniert. Beispiele können RSAT-/ActiveDirectory- oder ältere Hersteller-Module sein. Markiere solche Fälle klar als Windows-only.

## Setup-Verifikation

```powershell
$checks = [ordered]@{
    Pwsh = (Get-Command pwsh -ErrorAction SilentlyContinue) -ne $null
    Git = (Get-Command git -ErrorAction SilentlyContinue) -ne $null
    Code = (Get-Command code -ErrorAction SilentlyContinue) -ne $null
    PSScriptAnalyzer = (Get-Module PSScriptAnalyzer -ListAvailable) -ne $null
    Az = (Get-Module Az.Accounts -ListAvailable) -ne $null
    Graph = (Get-Module Microsoft.Graph.Authentication -ListAvailable) -ne $null
}
[pscustomobject]$checks
```
