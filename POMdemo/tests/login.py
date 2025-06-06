from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

#webdriver Path
g_chrome = "/Users/alfredoarredondo/Documents/Python/Selenium/WebDrivers/v137_0_7151_68/chromedriver-mac-arm64/chromedriver"  # Google Chrome
#Browser path
driver_path = g_chrome
#Configure the service
service_obj = Service(driver_path)
#Configure Google Chrome as Browser
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
usr_tbox = driver.find_element(By.NAME,"username")
psw_tbox = driver.find_element(By.NAME,"password")

usr_tbox.send_keys("Admin")
psw_tbox.send_keys("admin123")

lgn_button = driver.find_element(By.XPATH,"//*[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
lgn_button.click()

usr_drp_dwn = driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name")
usr_drp_dwn.click()

lgout = driver.find_element(By.LINK_TEXT,"Logout")
lgout.click()

time.sleep(3)

driver.close()
driver.quit()
print("Test Completed...")