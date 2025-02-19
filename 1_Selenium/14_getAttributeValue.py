
# ------------------- how to get Element Attribute Value -----------------------

# <tag attribute = "value"> content </tag>

# we can extract this value using selenium

# .get_attribute("attribute_Name")

# useCase --> to check if any partifular element is of submit type or not.



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class demo_AttributeValue:

    def AttributeValue(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://yatra.com")

        # we can use any element locator here
        attr_value = driver.find_element(
            By.XPATH, "//p[@title='Mumbai']"
        ).get_attribute("title")  

        time.sleep(3)

        print(attr_value)  # Mumbai
        

value = demo_AttributeValue()
value.AttributeValue()
