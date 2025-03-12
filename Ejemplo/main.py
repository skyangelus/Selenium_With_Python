from browser_config import BrowserConfig
from interact_browser import browserActions

'''
Clase principal en donde se ejecuta el programa
'''
#Setea la configuración general del navegador
b_cfg = BrowserConfig("Chrome") #Se crea una instancia de la clase BrowserConfig indicando que navegador vamos a usar
b_cfg.setup_browser() #Se setean las condiciones del navegador deseado haciendo una llamada al metodo setup_browser de la clase BrowserConfig

i_bwsr = browserActions(b_cfg.driver) #Se pasan las condiciones del driver a la clase browserActions por medio de una instancia
i_bwsr.navigate_to_google() #El navegador deseado es abierto y navega a Google
i_bwsr.search("Selenium with Python") #En la caja de busqueda de Google se manda una cadena de texto deseada
b_cfg.close_browser() #Cierrar el navegador