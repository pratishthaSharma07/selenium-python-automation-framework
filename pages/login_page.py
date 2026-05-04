from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.login = (By.LINK_TEXT, "Signup / Login")
        self.email = (By.XPATH, "//input[@data-qa='login-email']")
        self.password = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_btn = (By.XPATH, "//button[@data-qa='login-button']")
        self.logout_btn = (By.LINK_TEXT, "Logout")

    def login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.login))
        self.driver.find_element(*self.login).click()

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.email))
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password))
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn))
        self.driver.find_element(*self.login_btn).click()

    def click_logout_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.logout_btn))
        self.driver.find_element(*self.logout_btn).click()


        





