# python
Este espacio es creado para agregar varios scripts que he generado en Python y que me han ayudado en mi dia a dia como Data Analyst

* InsercionDatos.py <- En este ejercicio uso las librerias de random,string, y sqlite3. Lo que hice fue genrar datos al azar apartir de listas (Nombres y Apellidos), para el       campo RFC debia ser llenado por medio de una funcion que respete las reglas de como esta constituido un RFC (Registro Federal de Contribuyentes) que son:
    4 caracteres,6 numeros y 3 caracteres, es importante que los números sean consistentes con una fecha valida.

  Use funciones para generar los campos de acuerdo a la solicitud, me refiero a que para el RFC, cree tres campos el primero es el año el cual tiene un rango de 60 a 98, para     los siguientes campos fue pues el rango de 1 a 12 ya que era le mes y para día utilice el rango de 1 a 30, en estos use una función extra para que me colocara el 0 a la         izquierda si aplicaba. Después por medio de la librería sqlite3, inserte los datos a la bd, en una tabla que ya había creado,
