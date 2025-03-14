
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

'''
La Clase browserActions se encarga de interactuar con el navegador
'''

class browserActions:
    def __init__(self,driver):
        self.driver = driver

    try:
        def navigate_to_google(self):
            self.driver.get("https://www.google.com")
            print("Navegando a Google...")
        
        def search(self, query):
            search_box = self.driver.find_element(By.NAME,"q") #Asigna el elemento de la barra de busqueda a la variable search_box
            search_box.send_keys(query) #Escribe la consulta en la barra de busqueda de google

            #Evaluation
            assert search_box.get_attribute('value')
            print(f"Test 1 Succesfull!!!: The text in the search box \"{search_box.get_attribute('value')}\" is equal to \"{query}\"")

            search_box.send_keys(Keys.RETURN) #Presiona la tecla ENTER
            print(f"Buscando: {query}")

            time.sleep(3) #Espera a que se muestren resultados

    except NoSuchElementException:
        # Capturar la excepción si el elemento no se encuentra
        print("Error: The element was not found in the page.")

    except TimeoutException:
        # Capturar la excepción si la página tarda demasiado en cargar
        print("Error: The page took too long to load.")

    except Exception as e:
        # Capturar cualquier otra excepción
        print(f"An unexpected error happened: {e}")