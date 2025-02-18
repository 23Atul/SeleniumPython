
# ----------- B R O W S E R      C O M M A N D S    IN    S E L E N I U M -----------------

# Navigate to ----> driver.get("URL")  ---> method
# opens the URL in browser session

# Get Current URL  ----> driver.current_url ---> property
# read he current URL from the browser's address bar

# Back ---> driver.back() ---> method
# presses the browser's back button

# Forward ---> driver.forward() ---> method
# Press the browser's forward button

# Refresh Page ---> driver.refresh() ---> method
# refresh the current page

# Get Page Title ---> driver.title() ----> property
# read the current page title from browser

# Maximize Window ---> driver.maximize_window() ---> method
# enlarges the window, without blocking the OS's own menu and toolbars.

# Minimize Window ---> driver.minimize_window() ---> method
# minimizes the window of current browsing context.

# Full Screen Window ---> driver.fullscreen_window() ---> method
# fills the entire screen

# closing a window or tab ---> driver.close() ---> method 
# closes the current window

# Quitting the browser at the end of the session ---> driver.quit() ---> method
# closes all the window and tabs associated with the webDriver session.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoSeleniumLearning:

    def demo_browser_methods(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # goes to yatra.com home page

        # Navigate to ----> driver.get("URL")  ---> method
        driver.get("https://yatra.com")


        # Get Current URL  ----> driver.current_url ---> property
        print(driver.current_url)  # https://www.yatra.com/


        # Get Page Title ---> driver.title ----> property
        print(driver.title) #Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com

        # Maximize Window ---> driver.maximize_window() ---> method
        driver.maximize_window()


        # Minimize Window ---> driver.minimize_window() ---> method
        driver.minimize_window()


        # Full Screen Window ---> driver.fullscreen_window() ---> method
        driver.fullscreen_window()

        time.sleep(4)

        # Refresh Page ---> driver.refresh() ---> method
        driver.refresh()

        time.sleep(4)

        driver.get("https://google.com")

        time.sleep(4)

        # Back ---> driver.back() ---> method
        driver.back()

        time.sleep(4)

        # Forward ---> driver.forward() ---> method
        driver.forward()

        time.sleep(4)

        driver.back()

        # closing a window or tab ---> driver.close() ---> method
        driver.close()

        time.sleep(4)

        # Quitting the browser at the end of the session ---> driver.quit() ---> method
        driver.quit()




        time.sleep(4)


BrowserCommand = DemoSeleniumLearning()
BrowserCommand.demo_browser_methods()


