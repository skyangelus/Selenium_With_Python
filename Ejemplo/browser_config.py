from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

'''
Clase BrowserConfig: Se encarga de configurar el navegador y el WebDriver.
'''
#Clasee for configurate the browser
class BrowserConfig:
    def __init__(self,browser_name):
        #self.driver_path = driver_path #Crea una variable para tomar el valor de la ruta del webdriver
        self.browser_name = browser_name #Crea una variable para tomar el valor del nombre del navegador
        self.driver = None #Crea una variable vacia para el driver
    
    def setup_browser(self):
        if self.browser_name == "Chrome":
            #Configurate the ChromeDriver Service
            driver_path = "C:\WebDrivers\chromedriver-win64\chromedriver.exe"
            service = Service(driver_path)
            self.driver = webdriver.Chrome(service=service)
        
        elif self.browser_name == "Edge":
            #Configurate the EdgeDriver Service
            driver_path = "C:\WebDrivers\edgedriver-win64\msedgedriver.exe"
            service = Service(driver_path)
            self.driver = webdriver.Edge(service=service)

        print(f"Navegador {self.browser_name} configurado correctamente.")

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print(f"Navegador {self.browser_name} Cerrado.")