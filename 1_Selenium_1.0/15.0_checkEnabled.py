
# test scenerio --> login butto gets enabled only when we enter both id and password.
# in this case login button is in desabled state and gets its state active only when required values are entered

# how to check if element has enabled state
# we will check the state on this website --> https://accounts.pega.com/register
# attribute for any element which is dissabled is ---> disabled = "true" or disabled = "disabled"

# is_enabled() --> returns true if element is not disabled.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class demo_ElementState:

    def demo_enable_disable(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://accounts.pega.com/register")

        demoState = driver.find_element(
            By.XPATH, "//button[@id='edit-submit']").is_enabled()
        time.sleep(3)

        print(demoState)  # False



value = demo_ElementState()
value.demo_enable_disable()
