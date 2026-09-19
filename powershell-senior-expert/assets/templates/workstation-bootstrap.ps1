#requires -Version 7.0
[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(
    [Parameter()]
    [switch]$InstallCloudModules,

    [Parameter()]
    [switch]$ConfigureGit,

    [Parameter()]
    [ValidateSet('Local', 'Global')]
    [string]$GitConfigScope = 'Local',

    [Parameter()]
    [string]$GitUserName,

    [Parameter()]
    [string]$GitUserEmail
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

if (-not $IsWindows) {
    throw 'Dieses Bootstrap-Skript unterstützt ausschließlich Windows.'
}

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw 'winget wurde nicht gefunden. Installiere oder repariere zuerst den App Installer.'
}

function Install-WinGetPackage {
    [CmdletBinding(SupportsShouldProcess)]
    param([Parameter(Mandatory)][string]$Id)

    winget list --id $Id --exact --accept-source-agreements | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Information "Paket bereits vorhanden: $Id"
        return
    }

    if ($PSCmdlet.ShouldProcess($Id, 'winget-Paket installieren')) {
        winget install --id $Id --exact --source winget --accept-package-agreements --accept-source-agreements
        if ($LASTEXITCODE -ne 0) {
            throw "winget-Installation fehlgeschlagen: $Id"
        }
    }
}

function Install-RequiredModule {
    [CmdletBinding(SupportsShouldProcess)]
    param([Parameter(Mandatory)][string]$Name)

    if (Get-Module -Name $Name -ListAvailable) {
        Write-Information "Modul bereits vorhanden: $Name"
        return
    }

    if ($PSCmdlet.ShouldProcess($Name, 'PowerShell-Modul für CurrentUser installieren')) {
        Install-Module -Name $Name -Scope CurrentUser -Repository PSGallery -Force
    }
}

@(
    'Microsoft.PowerShell'
    'Microsoft.VisualStudioCode'
    'Git.Git'
    'Microsoft.WindowsTerminal'
) | ForEach-Object { Install-WinGetPackage -Id $_ }

if (Get-Command code -ErrorAction SilentlyContinue) {
    @(
        'ms-vscode.PowerShell'
        'ms-vscode.azure-account'
        'ms-azuretools.vscode-azureresourcegroups'
        'eamodio.gitlens'
        'editorconfig.editorconfig'
    ) | ForEach-Object {
        if ($PSCmdlet.ShouldProcess($_, 'VS-Code-Erweiterung installieren')) {
            code --install-extension $_
            if ($LASTEXITCODE -ne 0) {
                throw "VS-Code-Erweiterung konnte nicht installiert werden: $_"
            }
        }
    }
}

@(
    'PSScriptAnalyzer'
    'Microsoft.PowerShell.SecretManagement'
    'Microsoft.PowerShell.SecretStore'
) | ForEach-Object { Install-RequiredModule -Name $_ }

if ($InstallCloudModules) {
    @('Az', 'Microsoft.Graph', 'ExchangeOnlineManagement', 'MicrosoftTeams') |
        ForEach-Object { Install-RequiredModule -Name $_ }
}

if ($ConfigureGit) {
    if ([string]::IsNullOrWhiteSpace($GitUserName) -or [string]::IsNullOrWhiteSpace($GitUserEmail)) {
        throw 'GitUserName und GitUserEmail sind mit ConfigureGit erforderlich.'
    }

    if ($GitConfigScope -eq 'Local' -and -not (Test-Path -LiteralPath '.git')) {
        throw 'Für lokale Git-Konfiguration muss das aktuelle Verzeichnis ein Repository sein.'
    }

    $scopeArgument = if ($GitConfigScope -eq 'Global') { '--global' } else { '--local' }
    if ($PSCmdlet.ShouldProcess("Git-Konfiguration $GitConfigScope", 'Name und E-Mail setzen')) {
        git config $scopeArgument user.name $GitUserName
        git config $scopeArgument user.email $GitUserEmail
        if ($LASTEXITCODE -ne 0) {
            throw 'Git-Konfiguration ist fehlgeschlagen.'
        }
    }
}

[pscustomobject]@{
    Pwsh = [bool](Get-Command pwsh -ErrorAction SilentlyContinue)
    Git = [bool](Get-Command git -ErrorAction SilentlyContinue)
    Code = [bool](Get-Command code -ErrorAction SilentlyContinue)
    PSScriptAnalyzer = [bool](Get-Module PSScriptAnalyzer -ListAvailable)
    SecretManagement = [bool](Get-Module Microsoft.PowerShell.SecretManagement -ListAvailable)
}
