import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

from utilities.customLogger import LogGenerate

# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def select_element(self, locator, value):
        element = self.driver.find_element(*locator)
        Select(element).select_by_visible_text(value)
        return element
    
    def javascript_executor_element(self, locator, value):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click()", element)
        element.clear()
        element.send_keys(value)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def save_screenshot(self, name="capture"):
        self.logging = LogGenerate.logger_file()
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(".", "screenshots", filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        result = self.driver.save_screenshot(path)
        self.logging.info(f"Screenshot saved: {path}")
        return result