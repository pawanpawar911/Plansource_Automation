import pytest
import allure
import time
import random
import inspect
import json
import requests
import os
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from base_pages.login_page import LoginPage
from base_pages.employees_page import EmployeePage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGenerate

from selenium.webdriver.common.by import By

# read the json user data
with open("user_data.json", "r") as file:
    user_data = json.load(file)

@pytest.fixture(autouse=True)
def setup(request):
    """Fixture to initialize application instance and ensure logging at the end of each test."""

    # Finalizer ensures logging after each test execution (even on failure)
    def finalize():
        logger = LogGenerate.logger_file()
        logger.info(f"Test Complete: {request.node.name}")

    request.addfinalizer(finalize)
    
    
@allure.title("Login Page Logo Test")
@allure.description("This is test of login page logo")
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
        logger.info(f"Test Assertion: {driver.title} page logo is displayed.")
        
    except AssertionError as e:
        login_page.save_screenshot("home_page_failure")
        logger.error(f"Assertion failed: {e}")
        raise

    except AttributeError as e:
        login_page.save_screenshot("home_page_failure")
        logger.error(f"AttributeError: {e}")
        raise

    except Exception as e:
        login_page.save_screenshot("home_page_failure")
        logger.error(f"Unexpected error: {e}")
        raise
    
@allure.title("Login Page Test")
@allure.description("This is test of login page")        
def test_login_window_valid_cred(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    usrN = ReadConfig.get_valid_usrName()
    passW = ReadConfig.get_valid_passWord()
        
    try:
        login_page = LoginPage(driver) 
        login_page.enter_usrname(usrN)
        logger.info(f"Username entered: {usrN}")
        
        login_page.enter_password(passW)
        logger.info(f"Password entered: {passW}")
        
        login_page.click_login()
        logger.info("Clicked on Login button")

        expected_titles = [
            "Add Employee",
            "PlanSource Login",
            "New Dependent - Testing Plansource Client Benefits",
            "Dashboard",
            "PlanSource ben admin"
        ]

        assert driver.title in expected_titles, f"Expected one of {expected_titles}, but got '{driver.title}'"
        logger.info(f"Test Assertion: {driver.title}")
        
    except AssertionError as e:
        login_page.save_screenshot("login_page_failure")
        logger.error(f"Assertion failed: {e}")
        raise

    except AttributeError as e:
        login_page.save_screenshot("login_page_failure")
        logger.error(f"AttributeError: {e}")
        raise

    except Exception as e:
        login_page.save_screenshot("login_page_failure")
        logger.error(f"Unexpected error: {e}")
        raise
        
@allure.title("Dashboard Page Test")
@allure.description("This is test of dashboard page-add new employee")        
def test_add_new_employee(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    try:
        employee_page = EmployeePage(driver) 
        employee_page.add_new_employee()
        logger.info("Clicked on Add New Employee")
        
        expected_titles = [
            "Add Employee",
            "New Dependent - Testing Plansource Client Benefits",
            "Dashboard",
            "PlanSource ben admin"
        ]

        assert driver.title in expected_titles, f"Expected one of {expected_titles}, but got '{driver.title}'"
        logger.info(f"Test Assertion: {driver.title}")

    except AssertionError as e:
        employee_page.save_screenshot("new_employee_failure")
        logger.error(f"Assertion failed: {e}")
        raise

    except AttributeError as e:
        employee_page.save_screenshot("new_employee_failure")
        logger.error(f"AttributeError: {e}")
        raise

    except Exception as e:
        employee_page.save_screenshot("new_employee_failuress")
        logger.error(f"Unexpected error: {e}")
        raise
    
@allure.title("Add New Employee Test")
@allure.description("This is test of add new employee deatils")   
def test_add_new_employee_details(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    passW = ReadConfig.get_valid_passWord()
        
    try:
        ssn = random.randint(100_000_000, 999_999_999)
        employee_page = EmployeePage(driver) 
        
        employee_page.enter_password(passW)
        logger.info(f"Password entered: {passW}")
        
        employee_page.add_firstname(user_data["firstname"])
        logger.info(f"First Name entered: {user_data["firstname"]}")
        
        employee_page.add_middlename(user_data["middlename"])
        logger.info(f"Middle Name entered: {user_data["middlename"]}")
        
        employee_page.add_lastname(user_data["lastname"])
        logger.info(f"Last Name entered: {user_data["lastname"]}")
        
        employee_page.ssn_id(ssn)
        logger.info(f"SSN entered: {ssn}")
        
        employee_page.add_address(user_data["address_1"])
        logger.info(f"Address entered: {user_data["address_1"]}")
        
        employee_page.add_city(user_data["city_name"])
        logger.info(f"City entered: {user_data["city_name"]}")
        
        employee_page.add_state(user_data["state"])
        logger.info(f"State entered: {user_data["state"]}")
        
        employee_page.add_zipcode(user_data["zip"])
        logger.info(f"Zipcode entered: {user_data["zip"]}")
        
        employee_page.add_country(user_data["country"])
        logger.info(f"Country entered: {user_data["country"]}")
        
        employee_page.add_email(user_data["email"])
        logger.info(f"Email entered: {user_data["email"]}")
        
        employee_page.preferred_communication(user_data["communication_mode"])
        logger.info(f"Communication mode entered: {user_data["communication_mode"]}")
        
        employee_page.add_birthdate(user_data["birthdate"])
        logger.info(f"Birthdate entered: {user_data["birthdate"]}")
        
        employee_page.add_gender(user_data["gender_male"])
        logger.info(f"Gender entered: {user_data["gender_male"]}")
        
        employee_page.add_marital_status(user_data["status"])
        logger.info(f"marital Status entered: {user_data["status"]}")
        
        employee_page.add_hire_date(user_data["hiredate"])
        logger.info(f"Hire date entered: {user_data["hiredate"]}")
        
        employee_page.add_eligibility_period(user_data["eligibility_date"])
        logger.info(f"Eligibility date entered: {user_data["eligibility_date"]}")
        
        employee_page.add_employment_level(user_data["emp_level"])
        logger.info(f"Employment level entered: {user_data["emp_level"]}")
        
        employee_page.add_location(user_data["location"])
        logger.info(f"Location entered: {user_data["location"]}")
        
        employee_page.add_current_salary(user_data["current_salary"])
        logger.info(f"Current salary entered: {user_data["current_salary"]}")
        
        employee_page.add_benefit_salary(user_data["benefit_salary"])
        logger.info(f"Benefit salary entered: {user_data["benefit_salary"]}")
        
        employee_page.add_pay_rate(user_data["pay_rate"])
        logger.info(f"Pay rate entered: {user_data["pay_rate"]}")
        
        employee_page.add_payroll_schedule(user_data["payroll"])
        logger.info(f"Payroll entered: {user_data["payroll"]}")
        
        employee_page.save_button()
        logger.info(f"Clicked on Submit button")

        expected_titles = [
            "Add Employee",
            "New Dependent - Testing Plansource Client Benefits",
            "Dashboard"
        ]

        assert driver.title in expected_titles, f"Expected one of {expected_titles}, but got '{driver.title}'"
        logger.info(f"Test Assertion: {driver.title}")
        
    except AssertionError as e:
        employee_page.save_screenshot("add_new_employee_failure")
        logger.info(f"Assertion failed: {e}") 
    
    except AttributeError as e:
        employee_page.save_screenshot("add_new_employee_failure")
        logger.info(f"AttributeError failed: {e}")  
        
    except Exception as e:
        employee_page.save_screenshot("add_new_employee_failure")
        logger.error(f"Unexpected error: {e}")
        raise  

@allure.title("Benefits and Family Page Test")
@allure.description("This is test of benefits and family page")       
def test_benefits_and_family(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    try:
        ssn = random.randint(100_000_000, 999_999_999)
        employee_page = EmployeePage(driver) 

        employee_page.add_new_hire_enrollment()
        logger.info(f"Clicked on New hire enrollment button")
        
        employee_page.get_started_button()
        logger.info(f"Clicked on Get started button")
        
        employee_page.submit_button()
        logger.info(f"Clicked on submit button")
        
        employee_page.add_new_family_member()
        logger.info(f"Clicked on New Family member button")

        employee_page.add_firstname(user_data["sp_first_name"])
        logger.info(f"First name entered: {user_data["sp_first_name"]}")
        
        employee_page.add_middlename(user_data["sp_middle_name"])
        logger.info(f"Middle name entered: {user_data["sp_middle_name"]}")
        
        employee_page.add_lastname(user_data["sp_last_name"])
        logger.info(f"Last name entered: {user_data["sp_last_name"]}")
        
        employee_page.ssn_id_1(ssn)
        logger.info(f"SSN ID entered: {ssn}")

        employee_page.add_birthdate(user_data["birthdate"])
        logger.info(f"Birthdate entered: {user_data["birthdate"]}")
        
        employee_page.add_gender(user_data["gender_female"])
        logger.info(f"Gender entered: {user_data["gender_female"]}")
        
        employee_page.add_relationship(user_data["relationship"])
        logger.info(f"Relationship entered: {user_data["relationship"]}")
        
        employee_page.submit_button()
        logger.info(f"Clicked on Next: Review My Family button")
        
        try: 
            employee_page.submit_button()
            logger.info(f"Clicked on Next: Shop for benefits button")
            
        except StaleElementReferenceException:
            employee_page.submit_button()
            logger.warning("StaleElementReferenceException caught, retrying")
            logger.info(f"Clicked on Next: Shop for benefits button")

        expected_titles = [
            "Add Employee",
            "New Dependent - Testing Plansource Client Benefits",
            'My Benefits - Testing Plansource Client Benefits',
            "Dashboard"
        ]

        assert driver.title in expected_titles, f"Expected one of {expected_titles}, but got '{driver.title}'"
        logger.info(f"Test Assertion: {driver.title}")
        
    except AssertionError as e:
        employee_page.save_screenshot("benefits_failure")
        logger.info(f"Assertion failed: {e}")
    
    except AttributeError as e:
        employee_page.save_screenshot("benefits_failure")
        logger.info(f"AttributeError failed: {e}")
    
    except Exception as e:
        employee_page.save_screenshot("benefits_failure")
        logger.error(f"Unexpected error: {e}")
        raise
        
@allure.title("Add Medical Plan Test")
@allure.description("This is test of add medical plan")           
def test_add_medical_plan(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    try:
        employee_page = EmployeePage(driver)

        employee_page.add_medical_plan()
        logger.info(f"Clicked Add medical plan button")

        employee_page.update_cart()
        logger.info(f"Clicked on update cart button")
        
        employee_page.radio_subscriber_button()
        logger.info(f"Clicked on radio subscriber button")
        
        employee_page.swipe_right_button()
        logger.info(f"Clicked on radio subscriber button")
        
        employee_page.submit_button()
        logger.info(f"Clicked on save button")

    except AssertionError as e:
        employee_page.save_screenshot("medical_plan_failure")
        logger.error(f"Assertion failed: {e}")
        raise

    except AttributeError as e:
        employee_page.save_screenshot("medical_plan_failure")
        logger.error(f"AttributeError: {e}")
        raise

    except Exception as e:
        employee_page.save_screenshot("medical_plan_failure")
        logger.error(f"Unexpected error: {e}")
        raise

@allure.title("Add Dental Plan API Test")
@allure.description("This is test of add dental plan using put requests api")         
def test_add_dental_plan(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")
    
    employee_page = EmployeePage(driver) 

    apiurl = ReadConfig.get_api_url()
    referer = ReadConfig.get_referer()

    session_id_value = driver.get_cookie("_session_id")["value"]
    
    logger.info(f"session id value : {session_id_value}")
    
    cookie_dict = {'_session_id': session_id_value}
    headers = {
        'Referer': referer,
        'Content-Type': 'application/json'
    }
    
    with open("api_json_body.json", "r") as file:
        json_body = json.load(file)
    
    try:
        # PUT Request
        response = requests.put(
            apiurl,
            cookies=cookie_dict,
            headers=headers,
            json=json_body
        )

        if response.status_code == 200:
            logger.info(f"Status Code: {response.status_code}")
        else:
            logger.error(f"Status Code Mismatched: {response.status_code}")
            raise AssertionError(f"Expected 200, but got {response.status_code}")
        
        if 'Content-Type' in response.headers:
            content_type = response.headers['Content-Type']
            logger.info(f"Received Content-Type: {content_type}")
            assert content_type == "application/json; charset=utf-8", f"Unexpected Content-Type: {content_type}"
        else:
            raise AssertionError("Content-Type header not found in response")
        time.sleep(2)
    except AssertionError as e:
        employee_page.save_screenshot("api_failure")
        logger.info(f"Assertion failed: {e}")
        raise
    
    except AttributeError as e:
        employee_page.save_screenshot("api_failure")
        logger.info(f"AttributeError failed: {e}")
        raise
    
    except Exception as e:
        employee_page.save_screenshot("api_failure")
        logger.info(f"General error failed: {e}")
        raise
    
@allure.title("Admin Tab and Download Test")
@allure.description("This is test of admin tab>proceed to checkout and download button")     
def test_admin_proceed_and_download(driver):
    logger = LogGenerate.logger_file()
    logger.info(f"Starting Test: {inspect.currentframe().f_code.co_name}")

    try:
        employee_page = EmployeePage(driver)
        
        employee_page.menu_button()
        logger.info(f"Clicked on Menu button")

        employee_page.admin_tab()
        logger.info(f"Clicked on Admin tab button")
        
        employee_page.proceed_to_checkout_tab()
        logger.info(f"Clicked on Proceed to checkout button")
        
        employee_page.checkout_button()
        logger.info(f"Clicked on checkout button")
        
        employee_page.download_button()
        logger.info(f"Clicked on Download button")
        logger.info(f"File Downloaded at : {os.getcwd()}")
        time.sleep(2)

    except AssertionError as e:
        employee_page.save_screenshot("admin_download_failure")
        logger.error(f"Assertion failed: {e}")
        raise

    except AttributeError as e:
        employee_page.save_screenshot("admin_download_failure")
        logger.error(f"AttributeError: {e}")
        raise

    except Exception as e:
        employee_page.save_screenshot("admin_download_failure")
        logger.error(f"Unexpected error: {e}")
        raise