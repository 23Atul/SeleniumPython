
# single value select from dropdown
# here we will look how we can select a value from dropdown that allows only one value to get selected.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
from selenium.webdriver.support.select import Select # this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class DemoDropdown:

    def Dropdown(self):

        # we can select and unselect the radio button by .click() method
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://testautomationcentral.com/demo/dropdown.html")
        
        dropdown = driver.find_element(By.XPATH, "//div[@id='simple-dropdown']//select[@class='form-select block w-full mt-1']")
        dd = Select(dropdown)  # checks if the dropdown has a select and options in or not, if no it returns an exception error.
        
        # 1. select_by_index()
        dd.select_by_index(1)  # selects the 1st option in the select dropdown.
        time.sleep(2)

        # 2. select_by_value(value)
        dd.select_by_value("option2")  #<option value="option2">Option 2</option>
        time.sleep(2)

        # 3. select_by_visible_text("text")
        dd.select_by_visible_text("Option 3")  # selects the provided value from the dropdown
        time.sleep(2)


findbyXpath = DemoDropdown()
findbyXpath.Dropdown()
