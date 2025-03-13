
# 1. drag_and_drop(source: WebElement, target: WebElement) → ActionChains
# Holds down the left mouse button on the source element, then moves to the target element and releases the mouse button.

# 2. drag_and_drop_by_offset(source: WebElement, xoffset: int, yoffset: int) → ActionChains
# Holds down the left mouse button on the source element, then moves to the target offset and releases the mouse button.


import time
from selenium.webdriver.common.by import By  # to use By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver import ActionChains


class demo_dragDrop:

    def DragDrop(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(3)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem_drag = driver.find_element(By.ID, "draggable")
        elem_drop = driver.find_element(By.ID, "droppable")

# 1 --> drag and drop using element
        ActionChains(driver).drag_and_drop(elem_drag,elem_drop).perform()
        time.sleep(4)

# 2 --> drag and drop using co-ordinates.
        ActionChains(driver).drag_and_drop_by_offset(elem_drag,60,80).perform()
        time.sleep(4)


        

findXPATH = demo_dragDrop()
findXPATH.DragDrop()
