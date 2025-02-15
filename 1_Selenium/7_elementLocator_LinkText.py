
# ---- find element by Link Text or Partial Link Text -------------

# when we see any clicable text ie. <a href="#" >Click Me </a>

# to make the browser click on the "Click Me" text we use LinkText Locator

# find_element(By.LINK_TEXT, "link text")  : - finds the clickable text ie. link and clicks on it using .click() method.
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByLinkText:

    def locator_by_LinkText_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")  # goes to yatra.com home page

        driver.find_element(
            By.LINK_TEXT, "For Travel Agents").click()  # finds the  link text with "For Travel Agents" and clicks it

        time.sleep(1)


findbyLinkText = DemoFindElementByLinkText()
findbyLinkText.locator_by_LinkText_demo()
