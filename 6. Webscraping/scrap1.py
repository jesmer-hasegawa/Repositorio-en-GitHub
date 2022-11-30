# Importar modulos
import requests
# Jesus Homero Galindo Gaytan

# Obtener la informacion HTML de la URL

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get (URL)

# Imprimir el texto de la peticion GET

print(page.text)