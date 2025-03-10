
# double_click(on_element: WebElement | None=None)
# Double-clicks an element.

import time
from selenium.webdriver.common.by import By  # to use By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver import ActionChains


class demo_rightClick:

    def RightClick(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()

        elem = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        act_chain = ActionChains(driver)
        time.sleep(2)
        act_chain.double_click(elem).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']").click()
        time.sleep(3)


findXPATH = demo_rightClick()
findXPATH.RightClick()
