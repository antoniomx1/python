import csv
import pymysql
from concurrent.futures import ThreadPoolExecutor
from conetsionesreportescompleto import *


class Conexion:
    def __init__(self, db_config, sql_query, csv_filename):
        self.db_config = db_config
        self.sql_query = sql_query
        self.csv_filename = csv_filename

    def conectar_y_exportar(self):
        try:
            with pymysql.connect(**self.db_config) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.sql_query)
                    results = cursor.fetchall()

                with open(self.csv_filename, "w", newline="" ) as csvfile:
                    csv_writer = csv.writer(csvfile)
                    column_names = [i[0] for i in cursor.description] 
                    csv_writer.writerow(column_names)
                    csv_writer.writerows(results)

            print("Datos exportados exitosamente a", self.csv_filename)

        except pymysql.connector.Error as err:
            print("Error en la conexión o consulta:", err)

def manejar_conexion(config):
    db_config = {
        "user": config["user"],
        "host": config["host"],
        "port": config["port"],
        "password": config["password"],
        "database": config["dbname"],
    }
    sql_query = config["query"]
    csv_filename = "G:/Mi unidad/Reports/aulascompleto/reportecompleto/" + config["name"] + ".csv"

    conexion_obj = Conexion(db_config, sql_query, csv_filename)
    conexion_obj.conectar_y_exportar()


archivos_csv_generados = [config["name"] + ".csv" for config in listamarysql]

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(manejar_conexion, listamarysql)

