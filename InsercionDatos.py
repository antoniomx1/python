import random
import string
import sqlite3

# Creamos una funcion para que genere los datos de rfc de acuerdo a las especificaciones
def generar_rfc():
    letras = ''.join(random.choices(string.ascii_uppercase, k=4))
    numeros = ''.join(random.choices(string.digits, k=3))
    anio= random.randint(60, 98)
    mes= random.randint(1, 12)
    dia= random.randint(1, 30)
    return letras + str(anio) + str(mes).rjust(2, '0') + str(dia).rjust(2, '0') + numeros

# Creamos otra funcion para generar el numero de empleado de acuerdo a las especificaciones
def generar_numero_empleado(año_ingreso):
    anioingreso= random.randint(2010, 2023)
    area = random.randint(1, 12)
    contador = str(random.randint(0, 99)).zfill(4)  # Contador
    return str(anioingreso) + str(area).rjust(2, '0') + contador 


# Establemcemos la conexion a la bd, creada en sqlite3
conn = sqlite3.connect('organizacion.db')
cursor = conn.cursor()


# Generamos 200 registros random, usando un bucle for el cual iniciara en el registro  1 y termina en el 200
for identificador in range(1, 201):
    nombres = ['Juanito', 'Pancho', 'Ana', 'Elena','Karina','Jessica','Sara','Diana','Carmela','Fulgencio','Florencio','Ebodio']
    nombre= random.choice(nombres)
    apellidos = ['Tranquilino', 'Ponciano', 'Alegria', 'Sanchez','SantaCruz','Aguado','Bross','Ramones','Fernandez','Delossantos','Bergoglio','Maradona']
    ap_materno = random.choice(apellidos)
    ap_paterno = random.choice(apellidos)
    rfc = generar_rfc()
    año_ingreso = random.randint(2010, 2023)
    numero_empleado = generar_numero_empleado(año_ingreso)

    cursor.execute('''
        INSERT INTO Empleado (Identificador, Nombre, ApMaterno, ApPaterno, RFC, NumeroEmpleado)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (identificador, nombre, ap_materno, ap_paterno, rfc, numero_empleado))

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
