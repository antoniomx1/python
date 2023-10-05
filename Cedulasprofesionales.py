from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd




base = pd.read_csv('D:/Users/jvelazhe/Desktop/Licenciaturas/profesores/cedulas.csv',encoding='latin1')

# Iniciar el navegador
driver = webdriver.Chrome(executable_path=r"C:/Selenium/chromedriver.exe")

# Abrir la página web
driver.get('https://www.cedulaprofesional.sep.gob.mx/cedula/presidencia/indexAvanzada.action#')
driver.maximize_window()
time.sleep(3)


# Hacer clic en el menú desplegable
menu_desplegable = driver.find_element(By.CSS_SELECTOR, ".dropdown:nth-child(2) > .dropdown-toggle").click()

# Esperar un poco (para asegurarse de que el contenido se haya cargado)
time.sleep(2)  

# Ingresar la clave en el campo de búsqueda
cedulas = driver.find_element(By.LINK_TEXT, "Cédula").click()
time.sleep(2)  

for i in range(base.__len__()): 
    try:
        cedula = str(base.iloc[i]['Cedula'])
        print(cedula)
        busqueda = driver.find_element(By.XPATH, '//*[@id="mainContainer_tablist_tab1"]/span[1]').click()
        campo_busqueda = driver.find_element(By.ID, "idCedula").clear()
        campo_busqueda = driver.find_element(By.ID, "idCedula").send_keys(cedula)
        time.sleep(2) 
        boton = driver.find_element(By.ID, "dijit_form_Button_1_label").click()
        detalle = driver.find_element(By.CSS_SELECTOR, "#mainContainer_tablist_tab2 > .tabLabel").click()
        rows = driver.find_elements(By.CSS_SELECTOR, ".dojoxGridContent .dojoxGridRow")

        # Iniciar una lista para guardar los datos
        data = []

        # Iterar sobre cada fila
        for row in rows:
            # Extraer las celdas de cada fila
            cells = row.find_elements(By.TAG_NAME, "td")
            # Extraer el texto de cada celda y agregarlo a una lista temporal
            temp_data = [cell.text for cell in cells]
            # Sólo agregar la lista temporal a la lista de datos si al menos una de las celdas tiene contenido
            if any(cell.strip() for cell in temp_data):
                data.append(temp_data)
            
        with open('detalles.csv', 'a', encoding='latin1', newline='') as file:
            writer = csv.writer(file,lineterminator='\n')
            writer.writerows(data)

        time.sleep(2) 

    except Exception as e:
        print(f"Error al buscar cédula {cedula}. Detalles del error: {str(e)}")
        continue  



driver.quit()
