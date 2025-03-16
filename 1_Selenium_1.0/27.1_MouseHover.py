
# there are some cases where a mouse hover is very imp. for eg when mouse is hovered over a web element then only menu will appear which can be then interacted.

import time
from selenium.webdriver.common.by import By  # to use By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver import ActionChains


class demo_MouseHover:

    def MouseHover(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://unstop.com/")
        driver.maximize_window()
        
#
        # trying to aceess the element without mouse hover,
        # if we try to access those elements then it will throw an error as they are not accessable without hover.

        # locating the element on which we have to hover

        more_btn = driver.find_element(By.XPATH, "//span[@aria-label='Browse More Categories']")

        act_chain = ActionChains(driver) # creating obj of class ActionChains
        time.sleep(2)

        # action chain helps us to chain many actions one after another like, hover then double click the click.
        # so after every action is chained they are waiting in a queue to make them happen we write .perform()
        act_chain.move_to_element(more_btn).perform() # driver moves/hover over to the more button
        # the above hover action was performed after i added perform().

        time.sleep(3)

        # clicking on element which was not visible directly but visible when hovered.
        driver.find_element(By.XPATH, "//strong[@aria-label='Conferences']").click()

        time.sleep(3)


findXPATH = demo_MouseHover()
findXPATH.MouseHover()


# What Does .perform() Do?
# The .perform() method executes all the actions that were queued up using ActionChains. Without .perform(), Selenium only stores the actions but doesn't actually run them.

# In your case, when you wrote:

# python
# Copy
# Edit
# act_chain.move_to_element(more_btn) 
# Selenium prepared the hover action but didn't execute it.

# When you added:

# python
# Copy
# Edit
# act_chain.move_to_element(more_btn).perform()
# Selenium immediately executed the hover action, causing the dropdown menu to appear.