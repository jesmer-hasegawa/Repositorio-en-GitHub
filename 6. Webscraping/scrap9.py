# Importacion de modulos
import requests
from bs4 import BeautifulSoup
# Jesus Homero Galindo Gaytan


# Obtencion de los datos mediante peticion GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get (URL)

# Analizamos el contenido HTML con Beautifulsoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Buscar todos los elementos que el class "card-content”
job_elements = results.find_all("div", class_="card-content")

# Buscar cada elemento que tengan referencia de python_jobs
python_jobs = results.find_all(
	"h2", string=lambda text: "python" in text.lower()
)

# Y almacenarlo en python_jobs_elements
python_jobs_elements = [
	h2_element.parent.parent.parent for h2_element in python_jobs
]

# Mostrar informacion de python_jobs_elemnts
for job_element in python_jobs_elements:
	title_element = job_element.find("h2", class_="title")
	company_element = job_element.find("h3", class_="company")
	location_element = job_element.find("p", class_="location")
	print (title_element.text.strip())
	print (company_element.text.strip())
	print (location_element.text.strip())
	print()
