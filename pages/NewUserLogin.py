from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewUserLogin:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.login_page = (By.LINK_TEXT, "Signup / Login")
        self.user_name = (By.XPATH, "//input[@data-qa='signup-name']")
        self.user_email = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located(self.login_page))
        self.driver.find_element(*self.login_page).click()
        
    def enter_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.user_name))
        self.driver.find_element(*self.user_name).send_keys(name)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.user_email))
        self.driver.find_element(*self.user_email).send_keys(email)

    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_btn))
        self.driver.find_element(*self.signup_btn).click()
