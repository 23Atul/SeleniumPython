

# when we click on some web elements it opens up the new tab with new page.(like Naukri.com) 
# we will look how we can access the elemets on new page with switching the windows b/w two tabs.

# selenium assigns a unique id to each window ie. unique window handle to each tabs.



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time
# this helps us to check whether the select tag is present in web element or not so that methods we are using for select tag can be used.


class demoMultipleWindows:

    def MultipleWindows(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/")

        parentHandle = driver.current_window_handle   # assigns a unique id to the current window
        print(parentHandle)  # 723B96566AE557801A7B9A9BEEFA0BBF
 
        driver.find_element(
            By.XPATH, "//body/div[@id='__next']/div/div/div/div/div/div[@id='special_offer']/div/div[@title=' Flat 12% OFF (up to Rs. 1,800)']/div/div[1]").click()
        time.sleep(5)

        # opens to new window but the control is still on parent page only it has not moved to the new tab


        all_handle = driver.window_handles # returns list of all the handles ie. parent + child
        print(all_handle)  # ['723B96566AE557801A7B9A9BEEFA0BBF', '513463DB625D7E8187FF12C6BB77A4ED']

        for handle in all_handle:
            if handle != parentHandle:
                driver.switch_to.window(handle)  # switching the focus from parent window to the child window 
                lowest = driver.find_element(By.XPATH, "//a[@title='Offers']")
                time.sleep(5)
                lowest.click()
                time.sleep(3)
                driver.close()  # closes the open tab
                time.sleep(3)
                break
        
        driver.switch_to.window(parentHandle) # switching focus back to parent window.
        time.sleep(3)




       
findbyXpath = demoMultipleWindows()
findbyXpath.MultipleWindows()
