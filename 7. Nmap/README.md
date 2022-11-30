# Nmap

## automap.sh<br>
script en bash que contiene un menú con las siguientes opciones:
- **Escaneo de red:** Al seleccionar esta opción deberá ejecutar nmap para realizar un
escaneo en la subred proporcionada por el usuario y el resultado deberá guardarlo
en archivo.
- **Escaneo individual:** Al seleccionar esta opción deberá ejecutar nmap para realizar
un escaneo a una ip proporcionada por el usuario de manera que se pueda
$nmap **"--script ssl-ccs-injection <ip victima> -oN ccs_injections_test.txt"** para
determinar que servicios esta desplegando al momento del escaneo, se deberá
guardar el resultado en archivo.
- **Escaneo udp:** Al seleccionar esta opción deberá ejecutar nmap para realizar un
scaneo tipo UDP a la ip que proporcione el usuario, el resultado del escaneo debe
almacenarse en archivo.
- **Escaneo de script:** Al seleccionar esta opción deberá ejecutar un nmap con la
opción de script, de manera que el usuario proporcione el nombre del script y la
dirección ip sobre la que se realizará el escaneo, al igual que los casos anteriores
deberá guardar el resultado en archivo.
- **Salir:** Al seleccionar esta opción deberá desplegar un mensaje de despedida y
terminar la ejecución del script. 
