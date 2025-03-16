
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByClassName:

    def locator_by_ClassName_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        # goes to yatra.com home page
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        driver.find_element(
            # finds the web elements with similar className, if there are more than one sililar ClassName then it chooses the firdt one?
            # By.CLASS_NAME, "yt-sme-mobile-input required_field email-login-box").send_keys("haha@gmail.com")
            By.CLASS_NAME, "email-login-box").send_keys("haha@gmail.com")


        time.sleep(2)


findbyTagName = DemoFindElementByClassName()
findbyTagName.locator_by_ClassName_demo()

# Message: no such element: Unable to locate element: {"method":"css selector","selector":".yt-sme-mobile-input required_field email-login-box"}

# it will show an error. 
# yt-sme-mobile-input required_field email-login-box ---> this is not a single class but a combination of 2 or more classes that is why any operation performed on it will will not be applicable.
# so we simply remove all other class and use the class which is unique or which is required for our operation.
