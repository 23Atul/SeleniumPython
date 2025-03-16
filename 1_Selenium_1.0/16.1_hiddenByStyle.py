
# here we will look at the case when element is hidden using style=displaye:none

# url --> http://w3schools.com/howto/howto_js_toggle_hide_show.asp

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoHiddenElement:

    def hiddenByStyle(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("http://w3schools.com/howto/howto_js_toggle_hide_show.asp")

        # element is displayed when page loads
        display1= driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        time.sleep(2)
        print(display1)  # True # displayed by default


        # making element hidden by pressing button then checking is_displayed()
        driver.find_element(
            By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        display2 = driver.find_element(
            By.XPATH, "//div[@id='myDIV']").is_displayed()
        time.sleep(2)
        print(display2)  # False  # element gets hidden when button is clcked




findbyXpath = DemoHiddenElement()
findbyXpath.hiddenByStyle()
