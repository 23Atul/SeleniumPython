
# how to handle auto suggestion or auto complete

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.
from selenium.webdriver.common.keys import Keys  # to use By


class DemoAutoSuggest:

    def AutoSuggest(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")


# case 1 : ---> user enters the city name, city appears on top and he click enter

        depart_from = driver.find_element(
            By.XPATH, "// p[@title = 'New Delhi']")
        time.sleep(2)
        depart_from.click()
        time.sleep(2)
        enter_from = driver.find_element(
            By.XPATH, "//input[@id='input-with-icon-adornment']")
        enter_from.send_keys("New Delhi")
        time.sleep(2)
        enter_from.send_keys(Keys.TAB) # mimics the user pressing the Tab key on their keyboard. 
        time.sleep(2)
        enter_from.send_keys(Keys.ENTER)  # mimics the user pressing the Enter key on their keyboard.

        time.sleep(2)


        driver.find_element(By.TAG_NAME, "body").click() # ** imp step ---> closes the suggestion box by clicking on the body so that focus from 1st input box goes away.


# case 2 : ---> user enters few letters, list of similar names appears, user goes down and click on required field.

        going_to = driver.find_element(
            By.XPATH, "//p[@title='Mumbai']")
        time.sleep(2)
        going_to.click()
        time.sleep(2)
        enter_to = driver.find_element(
            By.XPATH, "//input[@id='input-with-icon-adornment']")
        enter_to.send_keys("New")
        time.sleep(2)

        search_results = driver.find_elements(By.XPATH,"//div[@class='MuiBox-root css-134xwrj']//ul[1]/div") # for the suggestion we have 11 div that holds the value so we have modified the XPATH accordingly.
        print(len(search_results))  # 11 # since we have used the find_elements so it will return the list of all the suggestions in the page matching that key so it returned the 11 places
    
        # searching the particular value in the  suggestion box.
        for res in search_results: 
            enter_to.send_keys(Keys.TAB)  # Move focus to the next option
            # enter_to.send_keys(Keys.ARROW_DOWN)  # Move focus down

            time.sleep(3)
            print(res.text)
            
            if "New York, (JFK)" in res.text:

                time.sleep(3)
                res.click()
                time.sleep(4)
                break

findbyXpath = DemoAutoSuggest()
findbyXpath.AutoSuggest()
