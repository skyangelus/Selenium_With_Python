#Importar las librerias necesarias
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import Locators

class LoginPage():
    def __init__(self,driver):#Este es el contructor def __init__(self) pero queremos agregar un segundo argumento que sera el "driver" de selenium, así que agregamos driver en los argumentos
        self.driver = driver
        self.username_textbox_name = Locators.username_textbox_name #Importamos desde la clase Locator el locator name para el username
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
    
    def enter_user_name(self, username):
        usr_name = self.driver.find_element(By.NAME,self.username_textbox_name)
        usr_name.clear()
        usr_name.send_keys(username)

    def enter_password(self, password):
        psword = self.driver.find_element(By.NAME,self.password_textbox_name)
        psword.clear()
        psword.send_keys(password)

    def click_login(self):
        lgn_button = self.driver.find_element(By.XPATH,self.login_button_xpath)
        lgn_button.click()
