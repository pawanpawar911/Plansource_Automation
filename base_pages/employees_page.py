from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from base_pages.base_page import BasePage
from utilities.locators import EmployeePageLocators
import time

class EmployeePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # inherited base class attributes and methods
        
        self.driver = driver
        self.locators = EmployeePageLocators
        
    def add_new_employee(self):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        wait.until(EC.element_to_be_clickable(self.locators.add_new_emp)).click()
    
    def enter_password(self, password):
        self.find_element(*self.locators.password_textbox).send_keys(password)
        
    def add_firstname(self, firstname):
        self.find_element(*self.locators.firstName).send_keys(firstname)
        
    def add_middlename(self, middlename):
        self.find_element(*self.locators.middleName).send_keys(middlename)
        
    def add_lastname(self, lastname):
        self.find_element(*self.locators.lastName).send_keys(lastname)
        
    def ssn_id(self, ssn):
        self.find_element(*self.locators.ssn).send_keys(ssn)
        
    def add_address(self, address_1):
        self.find_element(*self.locators.add1).send_keys(address_1)
        
    def add_city(self, city_name):
        self.find_element(*self.locators.city).send_keys(city_name)
        
    def add_state(self, state):
        self.find_element(*self.locators.state).send_keys(state)
        
    def add_zipcode(self, zip):
        self.find_element(*self.locators.zipcode).send_keys(zip)
        
    def add_country(self, country):
        self.find_element(*self.locators.country).send_keys(country)
        
    def add_email(self, email):
        self.find_element(*self.locators.email).send_keys(email)
        
    def preferred_communication(self, mode):
        self.select_element(self.locators.preferred_comm, mode)       

    def add_birthdate(self, birthdate):
        self.javascript_executor_element(self.locators.birthdatePick, birthdate)

    def add_gender(self, male):
        self.select_element(self.locators.gender, male) 
        
    def add_marital_status(self, status):
        self.select_element(self.locators.marital_status, status) 
        
    def add_hire_date(self, hiredate):
        self.javascript_executor_element(self.locators.hire_date, hiredate)
        
    def add_eligibility_period(self, eligibility_start_date):
        self.javascript_executor_element(self.locators.benefit_start_date, eligibility_start_date)
        
    def add_employment_level(self, emp_level):
        self.select_element(self.locators.employment_level, emp_level)
        
    def add_location(self, emp_level):
        self.select_element(self.locators.location, emp_level)
        
    def add_current_salary(self, current_salary):
        self.find_element(*self.locators.current_salary).send_keys(current_salary)
        
    def add_benefit_salary(self, benefit_salary):
        self.find_element(*self.locators.benefit_salary).send_keys(benefit_salary)
        
    def add_plan_year(self, ssn):
        self.find_element(*self.ssn).send_keys(ssn)
        
    def add_pay_rate(self, pay_rate):
        ele = self.find_element(*self.locators.pay_rate)
        ele.clear()
        ele.send_keys(pay_rate)
        
    def add_payroll_schedule(self, payroll):
        self.select_element(self.locators.payroll_id, payroll)
        
    def save_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.submit_button)).click()

    def add_new_hire_enrollment(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.new_hire_enrollment)).click()

    def get_started_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.get_started_page)).click()

    def add_new_family_member(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.add_family_member)).click()
        
    def family_first_name(self, firstname):
        self.find_element(*self.locators.firstName).send_keys(firstname)
        
    def family_middle_name(self, middlename):
        self.find_element(*self.locators.middleName).send_keys(middlename)
        
    def family_last_name(self, lastname):
        self.find_element(*self.locators.lastName).send_keys(lastname)
        
    def ssn_id_1(self, ssn):
        self.find_element(*self.locators.ssn_id).send_keys(ssn)
        
    def add_relationship(self, relation):
        self.find_element(*self.locators.relationship).send_keys(relation)
        
    def submit_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.submit_form)).click()
        
    def add_medical_plan(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.medical_plan)).click()
        
    def update_cart(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        element = wait.until(EC.element_to_be_clickable(self.locators.update_cart))
        self.driver.execute_script("arguments[0].click();", element)
        
    def radio_subscriber_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.radio_subscriber)).click()
        
    def swipe_right_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.swipe_right_next)).click()
        
    def menu_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.menu_button)).click()
        
    def admin_tab(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable(self.locators.admin))
        self.driver.execute_script("arguments[0].click();", element)
        
    def proceed_to_checkout_tab(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        element = wait.until(EC.element_to_be_clickable(self.locators.proceed_to_checkout))
        self.driver.execute_script("arguments[0].click();", element)
        
    def download_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.download)).click()
        
    def checkout_button(self):
        wait = WebDriverWait(self.driver, 15)  # Wait up to 15 seconds
        wait.until(EC.element_to_be_clickable(self.locators.checkout_button)).click()