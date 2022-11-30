import requests
from bs4 import BeautifulSoup
# Jesus Homero Galindo Gaytan

# Importacion de modulos
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get (URL)

# Obtencion de los datos mediante peticién GET
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#Analizamos el contenido HTML con Beautifulsoup
# Buscar todos los elementos que el class "card-content”
job_elements = results.find_all("div", class_="card-content")

# Buscar todos los elementos que el h2 contenga en su texto
# la palabra "python"
python_jobs = results.find_all(
"h2", string=lambda text: "python" in text.lower()
)

# buscamos y mostramos informaicon sobre los elementos de
# python_jobs
for job_element in python_jobs:
	title_element = job_element.find("h2", class_="title")
	company_element = job_element.find("h3", class_="company")
	location_element = job_element.find("p", class_="location")
	print (title_element.text.strip())
	print (company_element.text.strip())
	print (location_element.text.strip())
	print()
