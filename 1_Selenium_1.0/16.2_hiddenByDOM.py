
# here we will look at the case when element is hidden by DOM ie. element is destroyed by DOM when certian action is performed or condition is satisfied.

# url --> https://www.yatra.com/hotels  --> Rooms and Guests


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoHiddenElement:

    def hiddenByDOM(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/hotels")

        # when the count is increased from 0 then the element gets created in DOM and it returns True
        driver.find_element(By.XPATH, "//div[@class='position-relative css-1moc4w8']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1cerw6e']//div[2]//div[1]//ul[1]//li[2]").click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item css-1wxaqej']//div[@class='MuiBox-root css-0']//div[@class='MuiBox-root css-0']").is_displayed()
        time.sleep(2)

        print(elem) # True


        # trying to find the element when the count is still 0 will give and exception error.
        driver.find_element(By.XPATH, "//div[@class='position-relative css-1moc4w8']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1cerw6e']//div[2]//div[1]//ul[1]//li[2]").click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item css-1wxaqej']//div[@class='MuiBox-root css-0']//div[@class='MuiBox-root css-0']").is_displayed()
        time.sleep(2)

        print(elem) # Exception Error, no such element exists

        

findbyXpath = DemoHiddenElement()
findbyXpath.hiddenByDOM()
