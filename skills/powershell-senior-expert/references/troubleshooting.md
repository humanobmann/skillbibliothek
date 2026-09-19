# Troubleshooting

## Diagnose-Reihenfolge

1. PowerShell-Version und Plattform prüfen.
2. Modulverfügbarkeit und Modulversion prüfen.
3. Authentifizierungskontext prüfen.
4. Berechtigungen/Rollen/Scopes prüfen.
5. Netzwerk, Proxy, TLS und Endpunkte prüfen.
6. Minimal reproduzierbares Beispiel bauen.
7. Logs, `$Error[0]`, InnerException und Request-IDs sichern.

## Basisdiagnose

```powershell
$PSVersionTable
$IsWindows, $IsLinux, $IsMacOS
Get-ExecutionPolicy -List
Get-Module -ListAvailable | Sort-Object Name, Version | Select-Object Name, Version, Path
$env:PSModulePath -split [System.IO.Path]::PathSeparator
```

## Modulprobleme

```powershell
Get-Module <ModuleName> -ListAvailable | Sort-Object Version -Descending
Import-Module <ModuleName> -Verbose
Get-Command -Module <ModuleName>
```

Typische Ursachen:

- Modul wurde in Windows PowerShell installiert, aber in PowerShell 7 gesucht oder umgekehrt.
- Alte Version liegt früher in `$env:PSModulePath`.
- PowerShell Gallery/Proxy/TLS blockiert Installation.
- Modul ist Windows-only oder braucht Kompatibilitätsmodus.

## Authentifizierung

Azure:

```powershell
Get-AzContext
Get-AzTenant
Get-AzSubscription
```

Graph:

```powershell
Get-MgContext | Format-List *
```

Exchange:

```powershell
Get-ConnectionInformation
```

Teams:

```powershell
Get-CsTenant | Select-Object DisplayName, TenantId
```

Typische Ursachen:

- falscher Tenant
- falsche Subscription
- fehlender Scope oder Admin Consent
- Gastkonto statt nativer Tenant-Kontext
- Conditional Access oder MFA-Anforderung
- abgelaufene Session

## Netzwerk und Proxy

```powershell
Test-NetConnection powershellgallery.com -Port 443
Test-NetConnection graph.microsoft.com -Port 443
[Net.ServicePointManager]::SecurityProtocol
```

Bei Unternehmensproxy Proxy-Dokumentation der jeweiligen Module prüfen. Nicht blind TLS-/Zertifikatprüfungen deaktivieren.

## Skriptfehler analysieren

```powershell
$error[0] | Format-List * -Force
$error[0].Exception | Format-List * -Force
$error[0].ScriptStackTrace
```

Bei API-Fehlern Statuscode, Request-ID, Zeitstempel und Korrelation sichern.

## Minimalbeispiel

Reduziere Fehler auf:

```powershell
#requires -Version 7.2
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

try {
    # one failing command here
}
catch {
    $_ | Format-List * -Force
    throw
}
```

## Sichere Reparaturstrategie

- Erst lesen, dann ändern.
- Erst einzelne Testressource, dann Batch.
- Erst `-WhatIf`, dann produktiv.
- Vor Änderungen Export/Snapshot erzeugen.
- Rollback-Pfad dokumentieren.
