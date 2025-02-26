
# we can check or uncheck the checkbox/boxes using selenium
# tag --> input,   type --> checkbox
# <input type="checkbox">

# url -->  https://testautomationcentral.com/demo/checkboxes.html?utm_source=chatgpt.com#google_vignette

# for dynamic checkbox use ID insted of XPATH

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoCheckboxes:

    def checkbox(self):

        # we can check and uncheck the box by .click() method
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://testautomationcentral.com/demo/checkboxes.html?utm_source=chatgpt.com#google_vignette")
        time.sleep(2)
        driver.find_element(By.XPATH,"//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[1]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[2]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[3]/input[1]").click()
        time.sleep(2)

        # we can even find whether the checkbox is checked or not using is_selected()
        elem = driver.find_element(By.XPATH,"//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[1]/input[1]").is_selected()
        time.sleep(2)
        print(elem)  # True


        
findbyXpath = DemoCheckboxes()
findbyXpath.checkbox()
