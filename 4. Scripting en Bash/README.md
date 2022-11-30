# Scripting en Bash

### welcome.sh<br>
Muestra la fecha y el usuario del sistema

### bro.sh<br>
El comando read nos permite leer la entrada estándar en CLI, su sintaxis es así: read –p
“Mensaje” variable1 variable2 variableN .

### number.sh<br>
Lee 3 numeros asignados a variables para posteriormente mostrarlos.

### netdiscover.sh<br>
Script para descubrir los equipos conectados a la red interna.

### portscanv1.ps1<br>
script para escaneo de puertos

### superscan.sh<br>
Toma como referencia los anteriores para mostrar en sus opciones:
- **Netdiscover:** lo que deberá ejecutar netdiscover.sh<br>
- **Portscanv1:** lo que deberá ejecutar portscanv1.sh con todo y sus argumentos.<br>
$ chmod +x portscanv1.sh
$ ./portscanv1.sh
- **Welcome:** lo que deberá ejecutar welcome.sh<br>
- **Exit:** deberá permitir la salida del script.<br>
