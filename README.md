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
