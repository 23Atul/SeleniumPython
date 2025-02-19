# ------- we can access the text written in any web element -----------
# .text() methiod



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemogetText:

    def getText(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get("https://yatra.com")

        text = driver.find_element(
            By.XPATH, "//span[contains(text(),'*Offer valid on ICICI Bank Credit Cards Transactio')]"
            ).text # its a property not a method

        time.sleep(3)
        print(text)  #*Offer valid on ICICI Bank Credit Cards Transaction only.


elemText = DemogetText()
elemText.getText()
