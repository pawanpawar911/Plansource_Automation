import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.customLogger import LogGenerate
from selenium.webdriver.chrome.options import Options

location = os.getcwd()

@pytest.fixture(scope="session")
def driver():
    logger = LogGenerate.logger_file()
    logger.info("Starting application for the test session")
    
    options = Options()
    prefs = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection":False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-fullscreen")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    try: 
        yield driver
    finally:
        driver.quit()
        logger.info("Stopped application after the test session")