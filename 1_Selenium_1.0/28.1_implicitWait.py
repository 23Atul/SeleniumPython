
# how to handle auto suggestion or auto complete

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
# import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.
# from selenium.webdriver.common.keys import Keys  # to use By


class DemoImplicitWait:

    def ImplicitWait(self):

        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.get("https://login.salesforce.com/?locate=au")

# giving correct XPATH
        # driver.find_element(By.XPATH, "//input[@id='username']").send_keys("atulraman23")
        # time.sleep(2)

# giving wrong XPATH
        # driver.find_element(By.XPATH, "//input[@id='userame']").send_keys("atulraman23")
        # time.sleep(2)
        # NoSuchElementException: Message: no such element: Unable to locate element:

        # we do not want our code to give exception immediately so we will use wait.


        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.implicitly_wait(10) #-------------------------
        # 1. it will keep checking the presence of web elements in the page,
        # 2. if the element is found then it will not wait for 10 sec but move to further steps.
        # 3. if the element is not found even after 10 sec then it will show the exception error.
        # 4. implicit wait is applicable to all the web elements present in the script.
        # 5. does not let script to fail immdeiately in absense of web element.

        driver.get("https://login.salesforce.com/?locate=au")

        driver.find_element(By.XPATH, "//input[@id='username']").send_keys("atulraman23")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("xxxx")



findbyXpath = DemoImplicitWait()
findbyXpath.ImplicitWait()
