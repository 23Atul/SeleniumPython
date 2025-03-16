# handle iFrames
# <iframe></iframe>
# iframe helps us to insert one document model inside another model.
# like we can insert youtube video or pdf inside our webpage through iframe.
# eg. of iframe --> https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css

# just like multiple window, to interact with the elemets of iframe we need to first switch out focus to that particular iframe.


# element = driver.switch_to.active_element
# alert = driver.switch_to.alert
# driver.switch_to.default_content()
# driver.switch_to.frame('frame_name')
# driver.switch_to.frame(1)
# driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
# driver.switch_to.parent_frame()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class demo_handle_iFrames:

    def Handle_iFrames(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.get(
            "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()

        # switched to parent iframe
        # <iframe id = "iframeResult" name = "iframeResult" allowfullscreen = "true" xpath = "1" > </iframe >

        # 1. Switch with iframe locator
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

        # 2. Switch with ID
        # driver.switch_to.frame("iframeResult")

        # 3. Switch with name
        # driver.switch_to.frame("iframeResult")

        # 4. Switch with index
        # driver.switch_to.frame(0)


        time.sleep(3)
        # cant switch to this(child) frame from body, we need to first switch to parent forst, which we did in above lines.
        driver.switch_to.frame(0) # there are 3 iframes under parent iframe so we are choosing 1st.
        time.sleep(3)

        # parent iframe ---> child iframe ---> web element.click()
        driver.find_element(By.XPATH, "//a[normalize-space()='JAVASCRIPT']").click()
        time.sleep(3)


findbyXpath = demo_handle_iFrames()
findbyXpath.Handle_iFrames()
