
# ------- Partial Link Text --------------------

# if there are clickable texts which is partially clicable and half static. then for the we can apply partial click on static part.
# if there are multiple elements with matching text then it selects the first match.

# find_element(By.PARTIAL_LINK_TEXT, "partial link text")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByPartialLinkText:

    def locator_by_PartialLinkText_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")  # goes to yatra.com home page

        driver.find_element(
            # finds the  link text with "For Travel Agents" and clicks it
            By.PARTIAL_LINK_TEXT, "YRSBICEMI").click()

        time.sleep(1)


findbyPartialLinkText = DemoFindElementByPartialLinkText()
findbyPartialLinkText.locator_by_PartialLinkText_demo()
