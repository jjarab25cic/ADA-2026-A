param(
    [string]$CarpetaParejas = "D:\CIC\Programas\Algoritmos\gs_match\_gen_test",
    [string]$Python = "python"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$programa = Join-Path $scriptDir "stb_mtch_lab.py"

if (-not (Test-Path $programa)) {
    Write-Error "No se encontro el programa: $programa"
    exit 1
}

$archivos = Get-ChildItem -Path $CarpetaParejas -Filter "parejas*.txt" -File |
    Sort-Object { [int]([regex]::Match($_.BaseName, '\d+$').Value) }

if ($archivos.Count -eq 0) {
    Write-Error "No se encontraron archivos parejas*.txt en: $CarpetaParejas"
    exit 1
}

foreach ($archivo in $archivos) {
    Write-Host "Procesando $($archivo.FullName)"
    & $Python $programa --archivo $archivo.FullName

    if ($LASTEXITCODE -ne 0) {
        Write-Error "Fallo al procesar: $($archivo.FullName)"
        exit $LASTEXITCODE
    }
}

Write-Host "Proceso finalizado para $($archivos.Count) archivos."
