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
        driver.maximize_window()

        # in w3 school this alert part is in different frame so switching the frame.
        # switch with name
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        
    # we going to click the button to launch the popup box after every action   
    # till this step we are clicking on the button and popup appears, now how to handle that popup.

        # accept the alert ie. click on OK
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.accept() 
        time.sleep(2)
        
        # dismisses the alert ie. click on CANCEL
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        # use to send required user input in Prompt box.
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.send_keys("Atul")
        driver.switch_to.alert.accept()
        time.sleep(4)

        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text) # prints the text written in popup box
        # Please enter your name:





        


findbyXpath = demo_handleAlerts()
findbyXpath.HandleAlerts()
