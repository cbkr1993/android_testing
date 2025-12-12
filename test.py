from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium.options.android import UiAutomator2Options
from appium import webdriver
from time import sleep
import time


def test_google_search():
    # Launch Chrome (Selenium will try to manage the driver automatically)
    caps = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:platformVersion": "16",
    }
    options = UiAutomator2Options().load_capabilities(caps)

    driver = webdriver.Remote("http://127.0.0.1:4723",options=options,)
    # driver = webdriver.Chrome()


        #driver.maximize_window()
        #driver.get("https://www.google.com")

        # Accept cookies or extra dialog if needed (depends on region; you can handle later)

        # Find search box
        # search_box = driver.find_element(By.NAME, "q")
        # search_box.send_keys("Appium mobile automation")
        # search_box.send_keys(Keys.RETURN)
    driver.find_element("xpath", "//android.widget.TextView[@content-desc='Photos']").click()
    # driver.get("https://www.google.com")
    # assert "Google" in driver.title

    driver.quit()


# if __name__ == "__main__":
#     test_google_search()

# bhavana.chinnabalannagari@datafactz.com
# Targus12979769!
