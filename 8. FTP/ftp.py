#
# Script para transferencia de FTP
# Objetivo: Conectarse a servidor ftp y hacer un upload de un archivo.
# 25/10/2022 - v1 Jesus Homero Galindo Gaytan
#
# Importando modulo ftp
from ftplib import FTP
#
# Estableciendo conexion a servidor
#
ftp = FTP('192.168.1.75')
ftp.login('johnny','1899296')
ftp.cwd('upload')

# abrimos el archivo que vamos a enviar y lo guardamos
# en una variable
archivo = open('ADVERTENCIA.txt', 'rb')
#
# subir archivo
try:
	ftp.storlines('STOR ADVERTENCIA.txt', archivo)
	print("Se ha enviado el archivo!")
except Exception as e:
	print("No se pudo enviar el archivo")
