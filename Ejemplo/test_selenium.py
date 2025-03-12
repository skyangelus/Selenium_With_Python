from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Rutas de los distintos WebDrivers
g_Chrome = "C:\WebDrivers\chromedriver-win64\chromedriver.exe"
m_Edge = "C:\WebDrivers\edgedriver-win64\msedgedriver.exe"

# Ruta al WebDriver
driver_path = m_Edge

# Configurar el servicio y el navegador
service = Service(driver_path) #Configuera el Servicio
driver = webdriver.Chrome(service=service) #Configura Google Chrome como el navegador
driver = webdriver.Edge(service=service) #Configura Microsoft Edge como el navegador

# Abrir una página web
driver.get("https://www.google.com")

# Buscar un elemento e interactuar con él
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium con Python")
search_box.submit()

# Cerrar el navegador
driver.quit()