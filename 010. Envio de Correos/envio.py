import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Jesus Homero Galindo Gaytan

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

sender_email = str(input("Ingresa tu correo: "))
password = str(input("contraseña de aplicaciones: "))

receiver_email = str(input("Ingresa el correo del destinatario: "))
# establecer conexion con el servidor
server.login(sender_email,password)

message = MIMEMultipart("alternative")
message["Subject"] = "Prueba de envio (script Python) - <1899296>"
message["From"] = sender_email
message["To"] = receiver_email

html = """\
<html>
  <body>
  <p>"<h2>Practica 12</h2></p>
    <p>Ejercicio de la practica 12 para envio de correos</p>
    <p>
       <strong>Alumno:</strong> <Nombre de alumno><br>
       <strong>Matricula:</strong> <matricula><br>
       "
    </p>
  </body>
</html>
"""

part2 = MIMEText(html, "html")

message.attach(part2)

server.sendmail(sender_email,receiver_email,message.as_string())


# cerrar conexion
server.quit()
