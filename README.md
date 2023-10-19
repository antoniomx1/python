# python
Este espacio es creado para agregar varios scripts que he generado en Python y que me han ayudado en mi dia a dia como Data Analyst

* InsercionDatos.py <- En este ejercicio uso las librerias de random,string, y sqlite3. Lo que hice fue genrar datos al azar apartir de listas (Nombres y Apellidos), para el       campo RFC debia ser llenado por medio de una funcion que respete las reglas de como esta constituido un RFC (Registro Federal de Contribuyentes) que son:
    4 caracteres,6 numeros y 3 caracteres, es importante que los números sean consistentes con una fecha valida.
    Use funciones para generar los campos de acuerdo a la solicitud, me refiero a que para el RFC, cree tres campos el primero es el año el cual tiene un rango de 60 a 98,         para los siguientes campos fue pues el rango de 1 a 12 ya que era le mes y para día utilice el rango de 1 a 30, en estos use una función extra para que me colocara el 0 a      la izquierda si aplicaba. Después por medio de la librería sqlite3, inserte los datos a la bd, en una tabla que ya había creado. Para el campo numero de empleado se            requeria por medio de una función que reciba el
    último número de empleado y cumpla las siguientes reglas:
    Debe ser de 10 caracteres el número de empleado
    Los primeros 4 dígitos son del año de ingreso (genera aleatorios del 2010 al
    2023)
    Los siguientes 2 dígitos corresponden al identificador de área (en caso de
    que el identificador sea de un carácter rellena con ceros a la izquierda)
    Los siguientes 4 dígitos es un contador que comienza en 0000 y el siguiente
    número de empleado debe terminar con los dos últimos dígitos iguales
    (0000, 0011, 0022, 0033, ..., 0100)

* ExtraccionAulas <- El objetivo de este script es extraer informacion de BD en Mysql usando Python, especificamente la libreria de pymysql, ademas uso la libreria de              concurrent.futures, esta libreria me sirve para generar las consultas en 10 esquemas(BD) al mismo tiempo, asi se reduce el tiempo de extracción, ocupo dos modulos, en los      cuales   estoy detallando la conexion a esas BD y las consultas que aplico para extraer esa información.

* Cedulasprofesionales (Web Scraping con Selenium) <- Este código automatiza un proceso de búsqueda de cédulas profesionales en la pagina oficial de la sep . Para cada cédula presente en un archivo CSV, navega a la página, busca la cédula, extrae detalles y guarda esta información en otro archivo CSV llamado detalles.csv. Este ejemplo de web scraping, me es muy util ya que con esto puedo validar la cedula que nos comparte el docente es correcta.

* Correos <- Este codigo lo uso para enviar comunicados personalizados a cada docente, aparte de agregar un mensaje, adjunto un archivo, esto esde gran utilidad ya que disminuye el tiempo de envio de correos masivos a los docentes.
  





  
