

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByTagName:

    def locator_by_TagName_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        # goes to yatra.com home page
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        driver.find_element(
            # finds the  link text with "For Travel Agents" and clicks it
            By.TAG_NAME, "input").send_keys("haha@gmail.com")   # finds the web elements with similar tagname, if there are more than one sililar tagnames then it chooses the firdt one?
        

        time.sleep(1)


findbyTagName = DemoFindElementByTagName()
findbyTagName.locator_by_TagName_demo()
