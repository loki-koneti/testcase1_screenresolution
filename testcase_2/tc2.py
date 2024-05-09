from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By module
import time

def login_and_take_screenshot():
    url = "https://demo.dealsdray.com/"
    username = "prexo.mis@dealsdray.com"
    password = "prexo.mis@dealsdray.com"

   
    screenshot_path = "/home/hp/Videos/testcase_2/"  # Replace with your desired path

    
    driver = webdriver.Chrome()

    try:
        
        driver.get(url)

        time.sleep(2)  
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "btn-signin")

        
        email_input.send_keys(username)
        password_input.send_keys(password)

        
        
        login_button.click()

        time.sleep(5)  

        
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

    finally:
        
        driver.quit()

if __name__ == "__main__":
    login_and_take_screenshot()
