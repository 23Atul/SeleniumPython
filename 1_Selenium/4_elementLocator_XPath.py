# Locating web element by XPATH

# in can we are not able to find unique ID or NAME in web element. There are many dynamic web elements where we have to use XPATh to find the elements.


# Locating web element by XPATH

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByXPath:

    def locator_by_xpath_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        driver.find_element(
            By.XPATH, "//input[@id='login-input']").send_keys("alpha@gmail.com")

        time.sleep(3)


findbyID = DemoFindElementByXPath()
findbyID.locator_by_xpath_demo()
