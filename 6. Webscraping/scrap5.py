import requests
from bs4 import BeautifulSoup
# Importacion de modulos
# Jesus Homero Galindo Gaytan

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get (URL)

# Obtencion de los datos mediante peticién GET
soup = BeautifulSoup(page.content, "html.parser")
results = soup. find(id="ResultsContainer")

#Analizamos el contenido HTML con Beautifulsoup
job_elements = results.find_all("div", class_="card-content")


# En el objeto job_elemento buscamos solo aquellos elementos con
# titulo e informacién relevante.
for job_element in job_elements:
	title_element = job_element.find("h2", class_="title")
	company_element = job_element.find("h3", class_="company")
	location_element = job_element.find("p", class_="location")
	
	# Se imprime solo el texto.
	print (title_element.text)
	print (company_element.text)
	print (location_element.text)
	print()