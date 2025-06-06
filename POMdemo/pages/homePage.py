#Importar las librerias necesarias
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import Locators

class HomePage():
    def __init__(self,driver):#Este es el contructor def __init__(self) pero queremos agregar un segundo argumento que sera el "driver" de selenium, así que agregamos driver en los argumentos
        self.driver = driver
        self.welcome_link_name = Locators.welcome_link_name
        self.logout_link_linktext = Locators.logout_link_linktext

    def click_welcome(self):
        welcome_link = self.driver.find_element(By.CLASS_NAME,self.welcome_link_name)
        welcome_link.click()

    def click_logout(self):
        logout_opt = self.driver.find_element(By.LINK_TEXT,self.logout_link_linktext)
        logout_opt.click()