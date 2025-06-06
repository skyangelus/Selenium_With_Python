from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import unittest
from pages.loginPage import LoginPage #Del archivo loginPage.py importamos la clase LoginPage
from pages.homePage import HomePage #Del archivo homePage.py importamos la clase HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls): #setUpClass se ejecuta una sola vez antes de todos los métodos de prueba mientras que SetUp(self) se ejecutaría siempre antes de cada uno de los métodos
        #webdriver Path
        g_chrome = "/Users/alfredoarredondo/Documents/Python/Selenium/WebDrivers/v137_0_7151_68/chromedriver-mac-arm64/chromedriver"  # Google Chrome
        #Browser path
        driver_path = g_chrome
        #Configure the service
        service_obj = Service(driver_path)
        #Configure Google Chrome as Browser
        cls.driver = webdriver.Chrome(service = service_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver #Esto lo hacemos para no estar colocando self.driver en todas las sentencias
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_user_name("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        
        time.sleep(3)

    @classmethod
    def tearDownClass(cls): #tearDownClass(cls) Se ejecuta solo una vez, despues de que se completen todas las pruebas mientras que tearDown(self) se ejecuta siempre despues de cada prueba
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...")
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/alfredoarredondo/Documents/Python/Selenium/Selenium_With_Python/POMdemo/reports'))