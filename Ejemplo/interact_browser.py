
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
La Clase browserActions se encarga de interactuar con el navegador
'''

class browserActions:
    def __init__(self,driver):
        self.driver = driver
    
    def navigate_to_google(self):
        self.driver.get("https://www.google.com")
        print("Navegando a Google...")
    
    def search(self, query):
        search_box = self.driver.find_element(By.NAME,"q") #Asigna el elemento de la barra de busqueda a la variable search_box
        search_box.send_keys(query) #Escribe la consulta en la barra de busqueda de google
        search_box.send_keys(Keys.RETURN) #Presiona la tecla ENTER
        print(f"Buscando: {query}")