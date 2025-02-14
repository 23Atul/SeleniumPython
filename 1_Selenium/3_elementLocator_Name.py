
# Locating web element by ID

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByName:

    def locator_by_name_demo(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        driver.find_element(By.NAME, "login-input").send_keys("XYZ@gmail.com")

        time.sleep(3)


findbyID = DemoFindElementByName()
findbyID.locator_by_name_demo()
