# Importamos fernet desde cryptography
#
from cryptography.fernet import Fernet
# Definicion de la funcion genwrite que genera una llave
# para cifrado
def genwrite():
	key = Fernet.generate_key()
	with open("pass.key", "wb") as key_file:
		key_file.write(key)

# Llamamos a la funcion para generar el archivo "pass.key"
# que contiene la lalve
genwrite()

# Definicion de la funcion call_key con la cual leemos
# el contenido del archivo "pass.key"

def call_key():
	return open("pass.key","rb").read()
#
# Ahora cifraremos un mensaje almacenado y codificado previamente
key = call_key()
banner = "Hola soy Jesus Homero!".encode()
a = Fernet(key)
coded_banner = a.encrypt(banner)
print(coded_banner)
#
# hora desciframos el mensaje previamente cifrado
key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)
#
#Fin del script
