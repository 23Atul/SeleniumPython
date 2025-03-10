
# there are some cases where a mouse hover is very imp. for eg when mouse is hovered over a web element then only menu will appear which can be then interacted.

import time
from selenium.webdriver.common.by import By  # to use By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


class demo_MouseHover:

    def MouseHover(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://unstop.com/")
        driver.maximize_window()
        

        # trying to aceess the element without mouse hover,
        # if we try to access those elements then it will throw an error as they are not accessable without hover.

        time.sleep(3)


findXPATH = demo_MouseHover()
findXPATH.MouseHover()