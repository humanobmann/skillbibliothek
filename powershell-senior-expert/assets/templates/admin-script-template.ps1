#requires -Version 7.2
[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$Name,

    [Parameter()]
    [switch]$PassThru
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

function Write-Step {
    param([Parameter(Mandatory)][string]$Message)
    Write-Information "[$(Get-Date -Format o)] $Message"
}

try {
    Write-Step "starting"

    # TODO: read current state first
    # $current = Get-Something -Name $Name -ErrorAction SilentlyContinue

    if ($PSCmdlet.ShouldProcess($Name, 'apply requested change')) {
        # TODO: perform safe change here
    }

    $output = [pscustomobject]@{
        Name = $Name
        Changed = $false
        Timestamp = Get-Date
    }

    if ($PassThru) {
        $output
    }

    Write-Step "finished"
}
catch {
    Write-Error -Message "script failed: $($_.Exception.Message)"
    throw
}
