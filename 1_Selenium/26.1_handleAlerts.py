# handle popups and alerts
# javascript popups and alerts can't be handled how we use to handle web elements.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class demo_handleAlerts:

    def HandleAlerts(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")

        # in w3 school this alert part is in different frame so switching the frame.
        # switch with name
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        




        


findbyXpath = demo_handleAlerts()
findbyXpath.HandleAlerts()
