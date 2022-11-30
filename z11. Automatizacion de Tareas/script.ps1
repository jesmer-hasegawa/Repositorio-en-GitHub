# Jesus Homero Galindo Gaytan
$envio = New-ScheduledTaskAction -Execute 'send_sysinfo.ps1'
$trigger = New-ScheduledTaskTrigger -Once -At 11:21am
Register-ScheduledTask -Action $envio -Trigger $trigger -TaskPath "Mis Tareas" -TaskName "Envio correo" -Description "Envio informacion a un correo"

