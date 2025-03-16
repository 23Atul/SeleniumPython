
# we will be seeing the case where we can select the multiple options from the select dropdown


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.
from selenium.webdriver.support.select import Select


class DemoDropdown:

    def Dropdown(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://testautomationcentral.com/demo/dropdown.html")

        driver.find_element(By.XPATH,"//button[normalize-space()='Multi-Select']").click()
        dropdown = driver.find_element(By.XPATH, "//select[@class='form-multiselect block w-full mt-1']")
        # checks if the dropdown has a select and options in or not, if no it returns an exception error.
        dd = Select(dropdown)

        time.sleep(2)

# FOR THE MULTI SELECT WE CAN SELECT MORE THAN ONE VALUE FROM THE SELECT OPTIONS.

        # 1. select_by_index()
        dd.select_by_index(0)  # selects the 1st option in the select dropdown.
        time.sleep(1)
        dd.select_by_index(1)  # selects the 1st option in the select dropdown.
        time.sleep(1)


        # 2. select_by_value(value)
        # <option value="option2">Option 2</option>
        dd.select_by_value("option5")
        time.sleep(1)
        dd.select_by_value("option4")
        time.sleep(1)


        # 3. select_by_visible_text("text")
        # selects the provided value from the dropdown
        dd.select_by_visible_text("Option 3")
        time.sleep(1)
        dd.select_by_visible_text("Option 4")
        time.sleep(1)


findbyXpath = DemoDropdown()
findbyXpath.Dropdown()
