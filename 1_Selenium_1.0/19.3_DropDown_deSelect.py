from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.
from selenium.webdriver.support.select import Select


class DemoDropdown:

    def Dropdown(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://testautomationcentral.com/demo/dropdown.html")

        driver.find_element(
            By.XPATH, "//button[normalize-space()='Multi-Select']").click()
        dropdown = driver.find_element(
            By.XPATH, "//select[@class='form-multiselect block w-full mt-1']")
        # checks if the dropdown has a select and options in or not, if no it returns an exception error.
        dd = Select(dropdown)

        time.sleep(2)


        dd.select_by_index(0)  # selects the 1st option in the select dropdown.
        time.sleep(1)
        dd.select_by_index(1)  # selects the 1st option in the select dropdown.
        time.sleep(1)

        dd.select_by_value("option5")
        time.sleep(1)
        dd.select_by_value("option4")
        time.sleep(1)

        dd.select_by_visible_text("Option 3")
        time.sleep(1)
        dd.select_by_visible_text("Option 4")
        time.sleep(1)

# 1. deselect_by_index(index) --->  deselects the selected option by their index
        dd.deselect_by_index(1)
        time.sleep(1)

# 2. deselect_by_value(value) ---> deselects the selected option by their value
        dd.deselect_by_value("option4")
        time.sleep(1)

# 3. deselect_by_visible_text("text") ---> deselect the selected option by their name/text
        dd.deselect_by_visible_text("Option 3")
        time.sleep(1)


# selecting the options again to implement deselect_all method.
        dd.select_by_index(0)  # selects the 1st option in the select dropdown.
        time.sleep(1)
        dd.select_by_index(1)  # selects the 1st option in the select dropdown.
        time.sleep(1)

        dd.select_by_value("option5")
        time.sleep(1)
        dd.select_by_value("option4")
        time.sleep(1)

        dd.select_by_visible_text("Option 3")
        time.sleep(1)
        dd.select_by_visible_text("Option 4")
        time.sleep(1)

# 4. deselect_all() ---> works only with multiple select, deselects the all selected value
        dd.deselect_all()
        time.sleep(1)


findbyXpath = DemoDropdown()
findbyXpath.Dropdown()
