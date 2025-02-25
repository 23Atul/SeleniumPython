
# in 15.0 we have seen how to check if element is disabled or not ie. using is_enabled() method

# here we will make that disabled element enable.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class demo_ElementState:

    def demo_enable_disable(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://accounts.pega.com/register")

        driver.find_element(By.XPATH,"//input[@id='edit-first-name-0-value']").send_keys("Atul")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='edit-last-name-0-value']").send_keys("Raman")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='edit-employer-0-value']").send_keys("Cognizant")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='edit-mail-0-value']").send_keys("atulraman3@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='edit-pass']").send_keys("Atul@2018")
        time.sleep(1)


        demoState = driver.find_element(By.XPATH, "//button[@id='edit-submit']").is_enabled()
        time.sleep(1)
        print(demoState)  # True

        driver.find_element(By.XPATH, "//button[@id='edit-submit']").click()
        time.sleep(2)



value = demo_ElementState()
value.demo_enable_disable()
