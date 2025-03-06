# we will try accessing the login button without filling the credintials and capture ss.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class demoCaptureScreenshot:

    def CaptureScreenshot(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        demo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        demo.screenshot("22.2_firstCapture.png")
        time.sleep(2)

        demo.click()
        time.sleep(2)

        driver.get_screenshot_as_file("22.3_secondCapture_error.png")
        time.sleep(2)

        driver.save_screenshot("22.4_thirdCapture.png")





findbyXpath = demoCaptureScreenshot()
findbyXpath.CaptureScreenshot()
