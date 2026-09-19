[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string]$SourcePath,

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$OutputRoot
)

$ErrorActionPreference = 'Stop'

$resolvedSource = (Resolve-Path -LiteralPath $SourcePath -ErrorAction Stop).Path
$sourceItem = Get-Item -LiteralPath $resolvedSource -Force
if ($sourceItem.PSIsContainer) {
    throw "SourcePath must identify an Affinity document, not a directory."
}

$allowedExtensions = @('.afdesign', '.afphoto', '.afpub')
$extension = $sourceItem.Extension.ToLowerInvariant()
if ($extension -notin $allowedExtensions) {
    throw "Unsupported source extension '$extension'. Expected .afdesign, .afphoto, or .afpub."
}

if ([string]::IsNullOrWhiteSpace($OutputRoot)) {
    $OutputRoot = Join-Path -Path $sourceItem.DirectoryName -ChildPath 'Affinity-Work'
}

$absoluteOutputRoot = [System.IO.Path]::GetFullPath($OutputRoot)
if (Test-Path -LiteralPath $absoluteOutputRoot -PathType Leaf) {
    throw "OutputRoot points to a file: $absoluteOutputRoot"
}

New-Item -ItemType Directory -Path $absoluteOutputRoot -Force | Out-Null
$resolvedOutputRoot = (Resolve-Path -LiteralPath $absoluteOutputRoot).Path

$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$safeBaseName = ($sourceItem.BaseName -replace '[^\p{L}\p{Nd}._-]+', '-')
$safeBaseName = $safeBaseName.Trim('-', '.', ' ')
if ([string]::IsNullOrWhiteSpace($safeBaseName)) {
    $safeBaseName = 'affinity-document'
}

$workspaceName = '{0}-work-{1}' -f $safeBaseName, $timestamp
$workspacePath = Join-Path -Path $resolvedOutputRoot -ChildPath $workspaceName
if (Test-Path -LiteralPath $workspacePath) {
    $workspacePath = Join-Path -Path $resolvedOutputRoot -ChildPath ('{0}-{1}' -f $workspaceName, ([guid]::NewGuid().ToString('N').Substring(0, 8)))
}

$workspaceItem = New-Item -ItemType Directory -Path $workspacePath
$exportsPath = Join-Path -Path $workspaceItem.FullName -ChildPath 'exports'
New-Item -ItemType Directory -Path $exportsPath | Out-Null

$workingFileName = '{0}-working{1}' -f $safeBaseName, $extension
$workingPath = Join-Path -Path $workspaceItem.FullName -ChildPath $workingFileName
if ([System.IO.Path]::GetFullPath($workingPath).Equals([System.IO.Path]::GetFullPath($resolvedSource), [System.StringComparison]::OrdinalIgnoreCase)) {
    throw 'Refusing to overwrite the source document.'
}

Copy-Item -LiteralPath $resolvedSource -Destination $workingPath -ErrorAction Stop
$copiedItem = Get-Item -LiteralPath $workingPath
if ($copiedItem.Length -ne $sourceItem.Length) {
    throw 'Working-copy size does not match the source document.'
}

[pscustomobject]@{
    source_path = $resolvedSource
    working_path = $copiedItem.FullName
    exports_path = (Get-Item -LiteralPath $exportsPath).FullName
    source_bytes = $sourceItem.Length
    working_bytes = $copiedItem.Length
    original_unchanged = $true
} | ConvertTo-Json -Depth 2
