# ---- To find multiple elements(these methods will return a list): ----

# -- -> find_elements

# find_elements(By.ID, "id")
# find_elements(By.NAME, "name")
# find_elements(By.XPATH, "xpath")
# find_elements(By.LINK_TEXT, "link text")
# find_elements(By.PARTIAL_LINK_TEXT, "partial link text")
# find_elements(By.TAG_NAME, "tag name")
# find_elements(By.CLASS_NAME, "class name")
# find_elements(By.CSS_SELECTOR, "css selector")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # to use By
import time


class DemoFindElementsByTagName:

    def locator_by_TagName_demo(self):

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        # goes to yatra.com home page
        driver.get("https://yatra.com")

        lista=driver.find_elements(By.TAG_NAME, "a")
        

        print(lista)  # prints all the <a> tag
        print(len(lista))  # 263


        # print the text associated with anchor tag
        for i in lista:
            print(i.text)
        
        # eg. <a href="#">Welcome to selenium</a>
        # here welcome to selenium is the text assosicated with a tag

        

        time.sleep(1) 


findbyTagName = DemoFindElementsByTagName()
findbyTagName.locator_by_TagName_demo()


# 268


# Zone By The Park Kol...
# Kolkata
# 5.0
# ₹5, 216
# 3102bce - A Vedic Re...
# Goa
# 5.0
# ₹5, 875
# The Park Chennai
# Chennai
# 5.0
# ₹17, 532


# Mumbai
# Starting from
# ₹8, 318
# Bangalore
# Starting from
# ₹10, 071
# Pune
# Starting from
# ₹8, 100
# Kolkata
# Starting from
# ₹9, 323
# Hyderabad
# Starting from
# ₹7, 750
# Goa
# Starting from
# ₹8, 790


# Top Destination...
# Starting from
# ₹12, 323
# Asia
# Starting from
# ₹12, 323
# Middle East
# Starting from
# ₹18, 651
# Europe
# Starting from
# ₹27, 409
# Africa
# Starting from
# ₹31, 205


# Adventure
# Plan my Trip
# MICE
# Plan my Trip
# Cruise
# Plan my Trip
# Villas & Stays
# Plan my Trip
# Luxury Trains
# Plan my Trip
# Monuments
# Plan my Trip
# Activites
# Plan my Trip
# Gift Voucher
# Plan my Trip
# Freight
# Plan my Trip
# Visa
# Plan my Trip
# Delhi to Sydney Flight
# Mumbai to Bangkok Flight
# Delhi to Singapore Flight
# Delhi to New york Flight
# Mumbai to London Flight
# Mumbai to Dubai Flight
# Delhi to Ahmedabad Flight
# Delhi to Kochi Flight
# Mumbai to Chennai Flight
# Delhi to Guwahati Flight
# Indore to Goa Flight
# Kolkata to Bangalore Flight
# Ahmedabad to Jaipur Flight
# Mumbai to Goa Flight
# Pune to Delhi Flight
# Bangalore to Goa Flight
# Bangalore to Delhi Flight
# Delhi to Goa Flight
# Delhi to Mumbai Flight
# Mumbai to Delhi Flight
# Indore to Delhi Flight
# Patna to Delhi Flight
# Delhi to Guwahati Flight
# Kolkata to Bangalore Flight
# Delhi to Ahmedabad Flight
# Delhi to Raipur Flight
# Bangalore to Lucknow Flight
# Mumbai to Ahmedabad Flight
# Lucknow to Delhi Flight
# Bangalore to Jaipur Flight
# Bangalore to Pune Flight
# Mumbai to Kochi Flight
# Delhi to Kochi Flight
# Delhi to Bangalore Flight
# Mumbai to Ayodhya Flight
# Delhi to Srinagar Flight
# Hyderabad to Ayodhya Flight
# Chennai to Delhi Flight
# Kolkata to Hyderabad Flight
# Delhi to Patna Flight
# Ahmedabad to Toronto Flight
# Delhi to Male Flight
# Dubai to Chandigarh Flight
# Dubai to Calicut Flight
# Lucknow to Dubai Flight
# Delhi to Kathmandu Flight
# Delhi to Paris Flight
# Doha to Kochi Flight
# Mumbai to Paris Flight
# Mumbai to Bali Flight
# Trichy to Singapore Flight
# Ahmedabad to Bangkok Flight
# Trivandrum to Dubai Flight
# Ahmedabad to Dubai Flight
# Dubai to Amritsar Flight
# Dubai to Mumbai Flight
# Doha to Mumbai Flight
# Doha to Delhi Flight
# Mumbai to Phuket Flight
# Delhi to Auckland Flight
# Flights
# International Airlines
# Domestic Airlines
# Hotels
# Trains
# Bus Booking
# Holidays
# International Holiday Packages
# India Holiday Packages
# Outstation Cabs
# Indian Monuments
# MICE


