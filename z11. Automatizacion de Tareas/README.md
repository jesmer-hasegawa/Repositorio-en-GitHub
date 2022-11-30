# Automatizacion de Tareas

## proc_mon.sh<br>
genera un archivo con nomenclatura procesos-<fecha>.log cuyo contenido es el resultado de
la ejecución de proc_mon.sh 

## script1.ps1<br>
script para programar una tarea que:
- TaskAction: ejecuta el script de powershell “send_sysinfo.ps1”
- Tasktrigger: El horario de ejecución queda a tu elección.
- TaskPath: MisTareas
- Taskname: “Enviar sysinfo”
- Description: “Envio de información del sistema” 
