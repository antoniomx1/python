from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import time

# Declaramos info de logueo y directorio
URL = "https://vici2.scalahed.com/vicidial/admin.php?ADD=999999"
USERNAME = "usuario1"
PASSWORD = "password"
DESCARGAS = 'directoriodondecaeladescarga'
CHROMEDRIVER = r"C:/Selenium/chromedriver.exe"
VICI = f"directoriodondesemoveraelarchivo.csv"

def therecsv(directorio):
    return [file for file in os.listdir(directorio) if file.endswith('.csv')]

def vicireport ():
    url_with_credentials = URL.replace("https://", f"https://{USERNAME}:{PASSWORD}@")
    driver = webdriver.Chrome(CHROMEDRIVER)  
    driver.get(url_with_credentials)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td:nth-child(4) > ul:nth-child(3) > li:nth-child(1) font"))).click()

    date_a = driver.find_element(By.NAME, "query_date")
    date_a.clear()
    date_a.send_keys("2023-10-16")

    date_b = driver.find_element(By.NAME, "end_date")
    date_b.clear()
    date_b.send_keys("2023-10-21")

    driver.find_element(By.XPATH, "//select[@name='group[]']/option[text()='SEG_DOC']").click()
    driver.find_element(By.XPATH, "//select[@name='user_group[]']/option[text()='-- ALL USER GROUPS --']").click()
    driver.find_element(By.NAME, "report_display_type").click()
    driver.find_element(By.XPATH, "//select[@name='report_display_type']/option[text()='TEXT']").click()

    driver.find_element(By.NAME, "SUBMIT").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "DOWNLOAD"))).click()
    print("Iniciando descarga de vici....")
    while not therecsv(DESCARGAS):
        time.sleep(1)
    
    print("Descarga Finalizada")
    driver.quit()

def moveryrenombrar():
    for filename in os.listdir(DESCARGAS):
        if filename.startswith("AGENT_TIME"):
            source = os.path.join(DESCARGAS, filename)
            shutil.move(source, VICI)
            print("Se movio el archivo de descargas a la carpeta de vici con el nombre: ")

if __name__ == "__main__":
    vicireport()
    moveryrenombrar()
