
# tag --> input,  type ---> radio
# <input type="radio">

# url --> https://testautomationcentral.com/demo/radiobuttons.html

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoRadioButton:

    def RadioButton(self):

        # we can select and unselect the radio button by .click() method
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://testautomationcentral.com/demo/radiobuttons.html")
        time.sleep(2)

        driver.find_element(By.XPATH, "//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[3]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[2]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[1]/input[1]").click()
        time.sleep(2)

        # we can even find whether the radio button is clicked or not using is_selected()
        elem = driver.find_element(By.XPATH, "//body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/label[3]/input[1]").is_selected()
        time.sleep(2)
        print(elem)  # False


findbyXpath = DemoRadioButton()
findbyXpath.RadioButton()
