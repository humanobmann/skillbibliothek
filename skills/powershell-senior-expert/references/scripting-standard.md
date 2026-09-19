# Scripting Standard

## Senior-Standard

Ein gutes PowerShell-Skript ist sicher, idempotent, gut parametriert, beobachtbar und testbar. Es verändert Systeme nicht überraschend.

## Standardstruktur

```powershell
#requires -Version 7.2
[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$InputPath,

    [Parameter()]
    [switch]$PassThru
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

begin {
    Write-Information "starting script"
}

process {
    try {
        if ($PSCmdlet.ShouldProcess($InputPath, 'process input')) {
            # work here
        }
    }
    catch {
        Write-Error -ErrorRecord $_
        throw
    }
}

end {
    Write-Information "finished script"
}
```

## Parameterregeln

- Verwende `[Parameter(Mandatory)]` nur, wenn wirklich nötig.
- Verwende `ValidateSet`, `ValidatePattern`, `ValidateRange` oder `ValidateScript` bei riskanten Eingaben.
- Verwende `[switch]` für boolesche Flags.
- Verwende `[System.IO.FileInfo]` und `[System.IO.DirectoryInfo]` nur, wenn Pfadbindung wirklich gewünscht ist; sonst `[string]` plus eigene Prüfung.
- Gib nie echte Geheimnisse als Default-Wert an.

## Fehlerbehandlung

- Setze `$ErrorActionPreference = 'Stop'`.
- Nutze `try/catch` um externe Aufrufe, API-Operationen und Schreiboperationen.
- Nutze `throw` nach Logging, wenn der Fehler die Aufgabe invalidiert.
- Gib Originalfehler nicht durch generische Meldungen verloren.

Muster:

```powershell
try {
    $result = Get-Thing -Id $Id -ErrorAction Stop
}
catch {
    $message = "failed to get thing with id '$Id': $($_.Exception.Message)"
    Write-Error $message
    throw
}
```

## Idempotenz

Vor `New-*`, `Set-*`, `Remove-*`, `Disable-*` immer Ist-Zustand prüfen.

```powershell
$existing = Get-Thing -Name $Name -ErrorAction SilentlyContinue
if ($null -eq $existing) {
    if ($PSCmdlet.ShouldProcess($Name, 'create thing')) {
        New-Thing -Name $Name
    }
}
else {
    Write-Information "thing already exists: $Name"
}
```

## Ausgabe

- Gib Objekte aus, nicht formatierte Strings.
- Verwende `Write-Information` für Fortschritt.
- Verwende `Write-Warning` für beachtenswerte Risiken.
- Verwende `Write-Verbose` für Debugdetails.
- Verwende `Write-Host` nur für interaktive UX, nicht für Automationsdaten.

## Sicherheit

- Keine Klartext-Passwörter, Tokens oder Client-Secrets im Skript.
- Keine sensiblen Werte ins Log schreiben.
- Secrets über SecretManagement, Key Vault, Managed Identity oder CI/CD-Secrets beziehen.
- Für destructive operations `SupportsShouldProcess` und `-WhatIf` nutzbar machen.
- Bei Cloud-Aktionen Tenant, Subscription, Environment und Account sichtbar verifizieren.

## Performance

- Keine ungebremsten `Get-*` über große Tenants ohne Filter/Paging.
- Nutze serverseitige Filter, wenn das Modul sie unterstützt.
- Sammle Ergebnisse in Listen statt ineffizientem `+=` in großen Schleifen.
- Bei API-Throttling Retry mit Backoff einplanen.

## Cross-Platform

- Keine Backslashes hart codieren; nutze `Join-Path`.
- Keine Windows-only-Befehle ohne Kennzeichnung.
- Prüfe `$IsWindows`, `$IsLinux`, `$IsMacOS`, wenn OS-Verhalten relevant ist.
- Für Cloud Shell keine lokalen Pfade, GUI-Prompts oder Windows-Tools voraussetzen.

## PSScriptAnalyzer

```powershell
Invoke-ScriptAnalyzer -Path . -Recurse -Severity Warning,Error
Invoke-Formatter -ScriptDefinition (Get-Content .\script.ps1 -Raw)
```

Fehler nicht nur kosmetisch behandeln. Bei Security-Regeln wie `AvoidUsingInvokeExpression` grundsätzlich Alternativen verwenden.

## Antwortformat für Skriptlieferungen

1. Kurzer Zweck
2. Voraussetzungen
3. Skript
4. Beispielaufrufe
5. Verifikation
6. Hinweise zu Rechten, Risiken und Rollback
