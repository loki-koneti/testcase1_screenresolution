from selenium import webdriver
import datetime
import os

website_url = "https://www.getcalley.com/"

resolutions = {
    'Desktop': [(1920, 1080), (1366, 768), (1536, 864)],
    'Mobile': [(360, 640), (414, 896), (375, 667)]
}

browsers = ['chrome', 'firefox', 'safari']


timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
base_dir = os.path.join(os.getcwd(), 'screenshots_' + timestamp)
custom_dir = "/home/hp/Videos/testcase_1/"

for browser in browsers:
    for device, resolutions_list in resolutions.items():
        for resolution in resolutions_list:
            
            if browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'firefox':
                driver = webdriver.Firefox()
            elif browser == 'safari':
                driver = webdriver.Safari()
            else:
                continue

            
            driver.set_window_size(*resolution)

            
            driver.get(website_url)

            
            screenshot_path = os.path.join(custom_dir, device, f"{resolution[0]}x{resolution[1]}")
            os.makedirs(screenshot_path, exist_ok=True)
            screenshot_file = os.path.join(screenshot_path, f"{browser}_{timestamp}.png")
            driver.save_screenshot(screenshot_file)

            
            driver.quit()
