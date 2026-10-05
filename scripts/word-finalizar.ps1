# Abre un .docx con Word, actualiza índice y campos, lo guarda y exporta el PDF al lado.
# Uso: powershell -File scripts/word-finalizar.ps1 <archivo.docx>
param([Parameter(Mandatory = $true)][string]$Docx)

$path = (Resolve-Path $Docx).Path
$pdf = [IO.Path]::ChangeExtension($path, '.pdf')
$w = New-Object -ComObject Word.Application
$w.Visible = $false
try {
    $d = $w.Documents.Open($path)
    foreach ($t in $d.TablesOfContents) { $t.Update() }
    $d.Fields.Update() | Out-Null
    # el índice cambia la paginación: segunda pasada para que los números queden bien
    foreach ($t in $d.TablesOfContents) { $t.UpdatePageNumbers() }
    $d.Save()
    $d.SaveAs2($pdf, 17)
    "paginas: " + $d.ComputeStatistics(2)
    "palabras: " + $d.ComputeStatistics(0)
    $d.Close($false)
} finally {
    $w.Quit()
}
