clear-host
Write-Host “Bienvenido a un ejemplo de codificacion / decodificacion base64 usando powershell" -ForegroundColor Green
Write-Host “Codificando un archivo de texto”
#
# Se va a leer el contenido del archivo de texto
#
$inputfile = "c:\script\secret.txt”
$fc = get-content $inputfile
$GB = [System.Text.Encoding]::UTF8.Getbytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green
#
# Decodificando contento de un archivo
#
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.Getstring([System.convert]::FromBase64string($etext)) | Out-File -Encoding "ASCII" c:\script\decode_secret.txt
$outfilel2 = get-content c:\script\decode_secret.txt
Write-Host "El texto decodificado es el siguiente:" -Foregroundcolor Green
Write-Host "DECODIFICADO:" $outfile12
