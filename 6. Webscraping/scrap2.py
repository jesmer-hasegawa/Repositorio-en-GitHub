# Importacion de modulos
import requests
from bs4 import BeautifulSoup

# Jesus Homero Galindo Gaytan

# Obtencién de los datos mediante peticién GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get (URL)

# Analizamos el contenido HTML con BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Formateamos la salida del objeto results de Beautifulsoup
print(results.prettify())