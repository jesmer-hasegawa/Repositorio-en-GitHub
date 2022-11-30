# Webscraping
Los scripts de esta carpeta son una practica basada en el sitio: http://quotes.toscrape.com/ el cual está
diseñado para webscraping además de que no se incumplen condiciones de uso. 

### scrape_quote.py<br>
Sirve para hacer una petición a la URL del sitio, analizar el contenido HTML y generar listas citas y autores para mostrar en pantalla y guardar en
un archivo.csv.

### scrap1.py<br>
Se conecta y trae la información de la URL.

### scrap2.py<br>
Utilizando BeautifulSoup se analizará el contenido y se comenzará a formatear la
información recibida.

### scrap3.py<br>
Comenzamos a buscar información en base a metadatos, por ejemplo, buscamos
elementos de class “card-content”.

### scrap4.py<br>
Nos sigue apareciendo mucho código HTML extra, por lo que ahora buscaremos títulos con
información más precisa.

### scrap5.py<br>
Seguimos viendo código HTML, si lo queremos la información procederemos
solo mostrando el texto del elemento a imprimir del objeto.

### scrap6.py<br>
El resultado del script anterior parece arrojar espacios en blanco extra, los
podemos limpiar haciendo un ajuste en esta sección.

### scrap7.py<br>
Si el interés en particular es buscar empleos que esta relacionados a desarrollo
de Python, entonces la forma de la búsqueda cambia.

### scrap8.py<br>
Si queremos información adicional sobre esos empleos, podrías intentar iterar sobre la
información que previamente estábamos desplegando.


### scrap9.py<br>
Realiza ajustes para poder encontrar la información que necesitamos.

### scrap10.py<br>
Agrega información de contacto o como ser candidato al mismo.

### scrap11.py<br>
Incluye en la salida el link de href.

### scrap12.py<br>
Finalmente, aunque nos muestra los dos elementos de href, en realidad solo nos interesa el
elemento de “Apply Here”, el cual podemos filtrar.

