# from top-level module import  element1........
from selenium import Webdriver
# from top-level module.submodul.submodul import  element1........
from selenium.Webdriver.common.keys import Keys
# from moduleName
import time

# My Facebook credentials
username = "ranu"
password = "ranu@123"

# My chromedrive path
driver_path = "C:/Windows/System32/chromedriver.exe"

# My  URL of the Facebook login page
facebook_url = "https://www.facebook.com/"

# Create ChromeOptions and set the executable path
chromeoptions = Webdriver.ChromeOptions()
chromeoptions.add_argument(f"executable_path={driver_path}")

# ceo  = c
driver = Webdriver.Chrome(options=chromeoptions)

try:
    # Open Facebook login page
    driver.get(facebook_url)
    
    # Find the username and password input fields by name
    username_field = driver.find_element("name", "email")
    password_field = driver.find_element("name", "pass")
    
    # Input your credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    # Wait for the login process to complete (adjust sleep time if necessary)
    time.sleep(5000000)
    
    # You can add further automation steps here
    
finally:
    # Close the browser window
    driver.quit()
