
# we have seen sliders in the select experince in naukri.com or price range slider in flipkart.


import time
from selenium.webdriver.common.by import By  # to use By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver import ActionChains


class demo_handleSliders:

    def HandleSliders(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty")
        driver.maximize_window()

        elem1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")

# sometimes same method do not work for all the sliders. so we will look into all the methods possible for sliders.
        # 1
        ActionChains(driver).drag_and_drop_by_offset(elem1,60,0).perform() # moves the slider by 60px in x direct and 0px in y dir.
        time.sleep(5)

        # 2
        ActionChains(driver).click_and_hold(elem2).pause(1).move_by_offset(-50,0).release().perform()  # moving in left dir ie. -ve right.
        time.sleep(5)

        # 3
        ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(20,0).release().perform()
        time.sleep(4)









        

findXPATH = demo_handleSliders()
findXPATH.HandleSliders()
