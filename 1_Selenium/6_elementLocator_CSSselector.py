
# when we encounter the dynamic web elements we use CSS Selector


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementByCSSselector:

    def locator_by_cssSelector_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        driver.find_element(
            By.CSS_SELECTOR, "#login-input").send_keys("beta@gmail.com")

        time.sleep(2)


findbyCSSselector = DemoFindElementByCSSselector()
findbyCSSselector.locator_by_cssSelector_demo()

