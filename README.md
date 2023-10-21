​# Python Scripts Útiles

Este espacio ha sido creado para compartir varios scripts en Python que me han facilitado las tareas diarias como Analista de Datos.

​## InsercionDatos.py
**Objetivo:** Generar e insertar datos aleatorios en una base de datos SQLite.

### Características Principales:
- Generación de datos a partir de listas de nombres y apellidos.
- El campo RFC se compone siguiendo un formato específico (4 caracteres, 6 números, 3 caracteres), asegurando números consistentes con fechas válidas.
- El número de empleado se construye siguiendo una serie de reglas detalladas.

### Librerías Utilizadas:
- random
- string
- sqlite3

​## ExtraccionAulas.py
**Objetivo:** Extraer información de diversas bases de datos en MySQL.

### Características Principales:
- Uso concurrente para consultas en 10 esquemas de base de datos simultáneamente, optimizando el tiempo de extracción.

### Librerías Utilizadas:
- pymysql
- concurrent.futures

​## Cedulasprofesionales (Web Scraping con Selenium)
**Objetivo:** Automatizar la búsqueda y extracción de cédulas profesionales en el sitio oficial de la SEP.

### Características Principales:
- Navega y busca cédulas específicas en la página.
- Extrae y guarda detalles de cada cédula en un archivo `detalles.csv`.
- Valida que la cédula proporcionada por un docente sea correcta.

### Librerías Utilizadas:
- selenium

​## Correos.py
**Objetivo:** Automatizar el envío de comunicados personalizados a docentes.

### Características Principales:
- Envía mensajes con un archivo adjunto a cada docente.
- Optimiza el proceso de envío masivo de correos.

### Librerías Utilizadas:
- pandas
- yagmail

​## DescargaPythonSelenium.py
**Objetivo:** Descargar reportes en CSV usando Selenium.

### Características Principales:
- Automatiza el proceso de acceso, selección de reportes, aplicación de filtros y descarga de reportes desde un portal específico.
- Una vez descargado el CSV, lo traslada a una ruta específica para análisis posterior.

### Librerías Utilizadas:
- selenium
