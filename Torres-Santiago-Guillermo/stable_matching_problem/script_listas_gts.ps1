param(
    [Parameter(Mandatory = $true)]
    [ValidateRange(1, [int]::MaxValue)]
    [int]$NumArchivos,

    [string]$Carpeta = "D:\CIC\Programas\Algoritmos\gs_match\_gen_test",

    [int]$Semilla
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonFile = Join-Path $scriptDir "listas_pref.py"

if (-not (Test-Path -LiteralPath $pythonFile)) {
    Write-Error "No se encontro listas_pref.py en: $pythonFile"
    exit 1
}

$pythonCmd = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } elseif (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { $null }

if (-not $pythonCmd) {
    Write-Error "No se encontro un interprete de Python (py o python) en PATH."
    exit 1
}

$argsList = @($pythonFile, "-n", $NumArchivos, "-c", $Carpeta)
if ($PSBoundParameters.ContainsKey("Semilla")) {
    $argsList += @("-s", $Semilla)
}

& $pythonCmd @argsList
exit $LASTEXITCODE
