from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class LoginPageLocators(object):
    
    homepage_logo = (By.XPATH, "//img[@alt='PlanSource']")        
    username_textbox = (By.NAME, "user_name")
    password_textbox = (By.NAME, "password")
    cred_msg = (By.XPATH, "//div[@class='col alert-content']")
    login_button = (By.NAME, "Submit")
    
    
class EmployeePageLocators(object):
    
    add_new_emp = (By.XPATH, "//a[normalize-space()='Add a New Employee']")        
    password_textbox = (By.ID, "password")
    firstName = (By.ID, "first_name")
    middleName = (By.ID, "middle_name")
    lastName = (By.ID, "last_name")
    ssn = (By.ID, "ssn_text")
    ssn_id = (By.ID, "ssn")
    add1 = (By.ID, "address_1")
    city = (By.ID, "city")

    zipcode = (By.ID, "zip_code")
    country = (By.ID, "countryTypeahead")
    email = (By.ID, "email")
    preferred_comm = (By.ID, "communication_mode")
    state = (By.ID, "stateTypeahead")
    
    birthdatePick = (By.ID, "birthdate") #js executor
    gender = (By.ID, "gender") #select
    marital_status = (By.ID, "marital_status") #select
    hire_date = (By.ID, "hire_date") #js
    benefit_start_date = (By.ID, "benefits_start_date")
    employment_level = (By.ID, "employment_level") #select
    location = (By.ID, "location")
    current_salary = (By.ID, "current_salary")
    benefit_salary = (By.ID, "benefit_salary")
    benefit_salary_select = (By.ID, "benefit_salary_select")
    pay_rate = (By.ID, "pay_rate")
    payroll_id = (By.ID, "org_payroll_id")
    submit_button = (By.ID, "btn_save")
    
    new_hire_enrollment = (By.XPATH, "//a[normalize-space()='New Hire Enrollment']")
    get_started_page = (By.XPATH, "//a[contains(text(), 'Get Started')]")
    add_family_member = (By.XPATH, "//a[normalize-space()='Add Family Member']")
    submit_form = (By.ID , "submit_form")
    relationship = (By.ID, "relationship")
    lives_home = (By.ID, "lives_at_home")
    alert = (By.CLASS_NAME, "alert-message")