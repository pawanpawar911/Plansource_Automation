import pytest
import time
import random
import inspect
from selenium.webdriver.support.ui import WebDriverWait
from base_pages.login_page import LoginPage
from base_pages.employees_page import EmployeePage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGenerate

from selenium.webdriver.common.by import By

user_data = {
    "firstname": "Roger",
    "middlename": "Nana",
    "lastname": "Woakes",
    "address_1": "62, WayStreet",
    "city_name": "Birmingham",
    "state": "Alabama",
    "zip": 35001,
    "country": "Colombia",
    "email": "example123@gmail.com",
    "birthdate" : "05/01/1997",
    "hiredate" : "06/11/2025",
    "eligibility_date" : "06/11/2025",
    "current_salary" : "450",
    "benefit_salary" : "800",
    "pay_rate" : "125000",
    "emp_level" : "F",
    "payroll" : "Semi-monthly",
    "communication_mode" : "Email",
    "location" : "SCA",
    "status" : "Married",
    "gender_male":"Male",
    "gender_female" : "Female",
    "sp_first_name" : "Sanvy",
    "sp_middle_name" : "Kumari",
    "sp_last_name" : "Woakes",
    "sp_birthdate" : "05/01/2000",
    "relationship" : "Spouse"
    
}

@pytest.fixture(autouse=True)
def setup(request):
    """Fixture to initialize application instance and ensure logging at the end of each test."""

    # Finalizer ensures logging after each test execution (even on failure)
    def finalize():
        logger = LogGenerate.logger_file()
        logger.info(f"Test Complete: {request.node.name}")

    request.addfinalizer(finalize)

def test_home_page(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")
    
    login_page = LoginPage(driver)
    
    baseURL = ReadConfig.getWebURL()
    logger.info(f"Opening URL: {baseURL}")
    
    login_page.open_page(baseURL)
    
    logger.info(f"Verifying {driver.title} page")
    
    try:
        logo = login_page.logo()
        assert logo.is_displayed(), logger.info(f"Logo is not present on the homepage")
        logger.info(f"{driver.title} page logo is displayed.")
    except AssertionError as e:
        logger.info(f"Assertion failed: {e}") 

    except AttributeError as e:
        logger.info(f"AttributeError failed: {e}")
        
def test_login_window_valid_cred(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    usrN = ReadConfig.get_valid_usrName()
    passW = ReadConfig.get_valid_passWord()
        
    try:
        login_page = LoginPage(driver) 
        login_page.enter_usrname(usrN)
        login_page.enter_password(passW)
        login_page.click_login()

        expected_text = driver.title
        print(driver.title)
        actual_text = "Dashboard"

        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info(f"Test Correct Credential : Passed :: {driver.title}")
        
    except AssertionError as e:
        logger.info(f"Assertion failed: {e}")
    
    except AttributeError as e:
        logger.info(f"AttributeError failed: {e}")
        
        
def test_add_new_employee(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    try:
        employee_page = EmployeePage(driver) 
        employee_page.add_new_employee()

        expected_text = driver.title
        print(driver.title)
        actual_text = "PlanSource ben admin"

        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info(f"Test Correct Credential : Passed :: {driver.title}")
        time.sleep(3)
    except AssertionError as e:
        logger.info(f"Assertion failed: {e}") 
    
    except AttributeError as e:
        logger.info(f"AttributeError failed: {e}")

def test_add_new_employee_details(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    passW = ReadConfig.get_valid_passWord()
        
    try:
        ssn = random.randint(100_000_000, 999_999_999)
        employee_page = EmployeePage(driver) 
        employee_page.enter_password(passW)
        employee_page.add_firstname(user_data["firstname"])
        employee_page.add_middlename(user_data["middlename"])
        employee_page.add_lastname(user_data["lastname"])
        employee_page.ssn_id(ssn)
        employee_page.add_address(user_data["address_1"])
        employee_page.add_city(user_data["city_name"])
        employee_page.add_state(user_data["state"])
        employee_page.add_zipcode(user_data["zip"])
        employee_page.add_country(user_data["country"])
        employee_page.add_email(user_data["email"])
        employee_page.preferred_communication(user_data["communication_mode"])
        employee_page.add_birthdate(user_data["birthdate"])
        employee_page.add_gender(user_data["gender_male"])
        employee_page.add_marital_status(user_data["status"])
        employee_page.add_hire_date(user_data["hiredate"])
        employee_page.add_eligibility_period(user_data["eligibility_date"])
        employee_page.add_employment_level(user_data["emp_level"])
        employee_page.add_location(user_data["location"])
        employee_page.add_current_salary(user_data["current_salary"])
        employee_page.add_benefit_salary(user_data["benefit_salary"])
        employee_page.add_pay_rate(user_data["pay_rate"])
        employee_page.add_payroll_schedule(user_data["payroll"])
        employee_page.save_button()

        expected_text = driver.title
        print(driver.title)
        actual_text = "Add Employee"

        # time.sleep(8)
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info(f"Test Correct Credential : Passed :: {driver.title}")
    except AssertionError as e:
        logger.info(f"Assertion failed: {e}") 
    
    except AttributeError as e:
        logger.info(f"AttributeError failed: {e}")     
    
def test_add_new_enrollment_add_family(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    try:
        ssn = random.randint(100_000_000, 999_999_999)
        employee_page = EmployeePage(driver) 

        employee_page.add_new_hire_enrollment()
        # time.sleep(4)
        employee_page.get_started_button()
        # time.sleep(4)
        employee_page.submit_button()

        employee_page.add_new_family_member()

        employee_page.add_firstname(user_data["sp_first_name"])
        employee_page.add_middlename(user_data["sp_middle_name"])
        employee_page.add_lastname(user_data["sp_last_name"])
        employee_page.ssn_id_1(ssn)

        employee_page.add_birthdate(user_data["birthdate"])
        employee_page.add_gender(user_data["gender_female"])
        employee_page.add_relationship(user_data["relationship"])
        employee_page.submit_button()

        expected_text = driver.title
        print(driver.title)
        actual_text = "Add Employee"

        time.sleep(5)
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info(f"Test Correct Credential5 : Passed :: {driver.title}")
    except AssertionError as e:
        raise AssertionError(logger.info(f"Assertion failed: {e}"))
    
    except AttributeError as e:
        raise AttributeError(logger.info(f"AttributeError failed: {e}"))
    
    except Exception as e:
        logger.info(f"General error failed: {e}")