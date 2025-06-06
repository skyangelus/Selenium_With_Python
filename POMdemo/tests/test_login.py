from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import unittest

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
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        usr_tbox = self.driver.find_element(By.NAME,"username")
        psw_tbox = self.driver.find_element(By.NAME,"password")

        usr_tbox.send_keys("Admin")
        psw_tbox.send_keys("admin123")

        lgn_button = self.driver.find_element(By.XPATH,"//*[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
        lgn_button.click()

        usr_drp_dwn = self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name")
        usr_drp_dwn.click()

        lgout = self.driver.find_element(By.LINK_TEXT,"Logout")
        lgout.click()

        time.sleep(3)

    @classmethod
    def tearDownClass(cls): #tearDownClass(cls) Se ejecuta solo una vez, despues de que se completen todas las pruebas mientras que tearDown(self) se ejecuta siempre despues de cada prueba
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...")
        
if __name__ == '__main__':
    unittest.main()