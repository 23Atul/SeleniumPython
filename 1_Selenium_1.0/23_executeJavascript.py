
# JS is scripting lang which runs on client side.

# we can use JS to do the same activity which was done using selenium,
# even some activity which is very tough using selenium can vbe acieved very easily using JS
# if some element is hidden then interacting with it using selenium is tough job, but using JS we can easily interact with it.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class demoJavascript:

    def demo_JS(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # in selenium we use get()
        # driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        # in js
        # driver.execute_script("window.open('https://www.rcvacademy.com/')") # 2 tab gets opened 
        time.sleep(4)

        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');") # opens url in 1 tab only
        time.sleep(3)

        # click using JS  # similar to get element by tag name
        demoElement = driver.execute_script("return document.getElementsByTagName('a')[77]")
        time.sleep(5)

        # print(demoElement)
        driver.execute_script("arguments[0].click();",demoElement)
        time.sleep(2)
        

findbyXpath = demoJavascript()
findbyXpath.demo_JS()
