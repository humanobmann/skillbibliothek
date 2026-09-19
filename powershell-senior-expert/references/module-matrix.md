# Module Matrix

## Entscheidungsregel

Wähle das kleinste geeignete Modul. Bevorzuge stabile, offiziell gepflegte Module für produktive Administration. Nutze Preview/Beta nur bewusst und kennzeichne Risiken.

## Kernmodule

| Bereich | Modul | Zweck | Installation | Verbindung / Prüfung |
|---|---|---|---|---|
| Azure Resource Management | `Az` | Azure Ressourcen, RBAC, Subscriptions, Key Vault, Storage | `Install-Module Az -Scope CurrentUser -Repository PSGallery -Force` | `Connect-AzAccount`; `Get-AzContext` |
| Microsoft Graph | `Microsoft.Graph` oder Submodule | Entra ID, Users, Groups, Apps, Devices, Reports | `Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force` | `Connect-MgGraph -Scopes ...`; `Get-MgContext` |
| Exchange Online | `ExchangeOnlineManagement` | Mailboxes, Transport, Compliance-Verbindungen | `Install-Module ExchangeOnlineManagement -Scope CurrentUser -Force` | `Connect-ExchangeOnline -UserPrincipalName <upn>` |
| Teams | `MicrosoftTeams` | Teams, Policies, Voice, Teams Admin | `Install-Module MicrosoftTeams -Scope CurrentUser -Force` | `Connect-MicrosoftTeams` |
| Script Quality | `PSScriptAnalyzer` | Linting, Best Practices, Formatierung | `Install-Module PSScriptAnalyzer -Scope CurrentUser -Force` | `Invoke-ScriptAnalyzer -Path . -Recurse` |
| Secrets | `Microsoft.PowerShell.SecretManagement` + `Microsoft.PowerShell.SecretStore` | Secret-Abstraktion und lokaler Vault | `Install-Module Microsoft.PowerShell.SecretManagement,Microsoft.PowerShell.SecretStore -Scope CurrentUser -Force` | `Get-SecretVault`; `Register-SecretVault ...` |
| Package Management | `Microsoft.PowerShell.PSResourceGet` | Module/Skripte finden, installieren, aktualisieren | meist in modernen PowerShell-Versionen vorhanden; sonst nachinstallieren | `Find-PSResource`, `Install-PSResource`, `Update-PSResource` |
| Windows Admin | `ActiveDirectory`, `DnsServer`, `GroupPolicy`, `Hyper-V` | RSAT-/Serververwaltung | über Windows Features/RSAT, nicht PSGallery-Default | `Get-Module -ListAvailable ActiveDirectory` |

## Microsoft Graph Scopes

Nie pauschal `Directory.ReadWrite.All` oder `User.ReadWrite.All` verwenden, wenn ein engerer Scope reicht. Gib Scopes explizit aus und erkläre Admin-Consent, wenn nötig.

Beispiele:

```powershell
Connect-MgGraph -Scopes 'User.Read.All','Group.Read.All'
Get-MgContext
```

Für schreibende Aktionen:

```powershell
Connect-MgGraph -Scopes 'User.ReadWrite.All'
```

Produktionsregel: App-only mit Zertifikat, Managed Identity oder workload identity bevorzugen, wenn Automationen unbeaufsichtigt laufen sollen.

## Azure

Interaktiv:

```powershell
Connect-AzAccount
Get-AzContext
Get-AzSubscription
```

Tenant/Subskription setzen:

```powershell
Set-AzContext -Tenant '<tenant-id>' -Subscription '<subscription-id-or-name>'
```

Automatisierung:

- Azure Automation: Managed Identity bevorzugen.
- GitHub Actions/Azure DevOps: OIDC/Federated Credentials bevorzugen.
- Lokale Skripte: keine Client-Secrets im Code; SecretManagement oder Key Vault verwenden.

## Exchange Online

```powershell
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName '<admin-upn>' -ShowBanner:$false
Get-ConnectionInformation
Disconnect-ExchangeOnline -Confirm:$false
```

Hinweise:

- Immer sauber trennen, damit Sessions nicht hängen bleiben.
- Für PowerShell 7 moderne Authentifizierung verwenden.
- Für unbeaufsichtigte Skripte App-only, Zertifikat oder Managed Identity prüfen.

## Teams

```powershell
Install-Module -Name MicrosoftTeams -Scope CurrentUser -Force
Connect-MicrosoftTeams
Get-Team
```

Bei Policy-/Voice-Themen immer zuerst Tenant-Kontext und Rollen prüfen.

## Intune

Nutze primär Microsoft Graph PowerShell oder Graph REST (`Invoke-MgGraphRequest`). Prüfe Endpunkte und Berechtigungen aktuell, weil Intune-Graph-Bereiche und Beta/v1.0-Verfügbarkeit sich ändern können.

Muster:

```powershell
Connect-MgGraph -Scopes 'DeviceManagementManagedDevices.Read.All'
Invoke-MgGraphRequest -Method GET -Uri 'https://graph.microsoft.com/v1.0/deviceManagement/managedDevices'
```

## Active Directory / RSAT

Für lokales AD ist das `ActiveDirectory`-Modul Windows-/RSAT-gebunden. In PowerShell 7 kann Kompatibilität funktionieren, aber robuste Admin-Runbooks sollten klar zwischen Windows PowerShell 5.1, PowerShell 7 und Remoting unterscheiden.

Prüfen:

```powershell
Get-Module -Name ActiveDirectory -ListAvailable
Get-Command Get-ADUser -ErrorAction SilentlyContinue
```

## Empfohlene Modulpflege

```powershell
# Inventar
Get-InstalledModule | Sort-Object Name | Select-Object Name, Version

# Updates prüfen
Get-InstalledModule | ForEach-Object {
    Find-Module -Name $_.Name -ErrorAction SilentlyContinue |
        Select-Object Name, Version
}

# Einzelnes Modul aktualisieren
Update-Module -Name Az -Force
```

Warnung: Module nicht blind mitten in Produktionssessions aktualisieren. Neue Shell öffnen, Breaking Changes prüfen, Skripte testen.
