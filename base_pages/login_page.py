import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.base_page import BasePage
from utilities.locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        
        self.driver = driver
        self.locators = LoginPageLocators
        
        super().__init__(driver)  # inherited base class attributes and methods
        
    def open_page(self, url):
        self.driver.get(url)
        
    def logo(self):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        return wait.until(EC.presence_of_element_located(self.locators.homepage_logo))
        
    def enter_usrname(self, username):
        self.find_element(*self.locators.username_textbox).send_keys(username)   
        
    def enter_password(self, password):
        self.find_element(*self.locators.password_textbox).send_keys(password)
        
    def login_msg(self):
        msg = self.find_element(*self.locators.cred_msg)
        return msg.text
        
    def click_login(self):
        self.find_element(*self.locators.login_button).click()