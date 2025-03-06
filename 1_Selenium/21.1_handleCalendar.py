

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class DemohandleCalendar:

    def handleCalendar(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")

        d_date = driver.find_element(By.XPATH, "//div[@class='css-w7k25o']")
        d_date.click()
        all_dates = driver.find_elements(By.XPATH, "//div[@class= 'react-datepicker__month-container']//div[@class='react-datepicker__month']//div[@class!='react-datepicker__day--disabled ']")
        time.sleep(2)
        
        for date in all_dates:
            # print(date.get_attribute("aria-label"))
            if date.get_attribute("aria-label") == "Choose Sunday, March 30th, 2025":
    
                date.click()
                time.sleep(2)


# //div[@class = 'react-datepicker__month-container']//div[@class = "react-datepicker__month"]//div[@class != "react-datepicker__day--disabled "]

findbyXpath = DemohandleCalendar()
findbyXpath.handleCalendar()





        

