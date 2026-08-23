# docx -> pdf -> png por pagina, para ver como queda el render. Version Windows.
# En macOS usar preview-docx.sh, que va por LibreOffice.
# Uso: powershell -File scripts/preview-docx.ps1 <archivo.docx> [directorio-salida]
param(
  [Parameter(Mandatory=$true)][string]$In,
  [string]$Out = "$env:TEMP\preview"
)
$ErrorActionPreference = 'Stop'
$In = (Resolve-Path $In).Path
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$base = [System.IO.Path]::GetFileNameWithoutExtension($In)
$pdf  = Join-Path $Out "$base.pdf"

# Word en vez de LibreOffice: es lo que suele estar instalado en Windows.
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
  $doc = $word.Documents.Open($In, $false, $true)
  $doc.SaveAs([ref]$pdf, [ref]17)   # 17 = wdFormatPDF
  Write-Output ("{0} paginas" -f $doc.ComputeStatistics(2))
  $doc.Close($false)
} finally {
  $word.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}

# pymupdf vive en el venv del proyecto
$py = Join-Path $PSScriptRoot "..\.venv\Scripts\python.exe"
& $py -c @"
import sys, pymupdf
pdf, out, base = sys.argv[1], sys.argv[2], sys.argv[3]
d = pymupdf.open(pdf)
for i, page in enumerate(d, 1):
    p = f'{out}/{base}_p{i:02d}.png'
    page.get_pixmap(dpi=110).save(p)
    print(' ', p)
"@ $pdf $Out $base
