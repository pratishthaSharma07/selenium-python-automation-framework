from pages.login_page import LoginPage 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_user(setup):
    driver = setup
    driver.get("https://automationexercise.com/")
    login_user = LoginPage(driver)
    email = "testautomation123@test.com"
    password = "tester@123"

    login_user.login_page()
    login_user.enter_email(email)
    login_user.enter_password(password)
    login_user.click_login_btn()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
    assert driver.find_element(By.LINK_TEXT, "Home").is_displayed()

def test_invalid_login(setup):
    driver = setup 
    driver.get("https://automationexercise.com/")
    invalid_login = LoginPage(driver)

    invalid_login.login_page()
    invalid_login.enter_email("wrong123@test.com")
    invalid_login.enter_password("wrong@123")
    invalid_login.click_login_btn()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']")))
    assert driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']").is_displayed()

def test_logout_btn(setup):
    driver = setup
    driver.get("https://automationexercise.com/")
    logout_user = LoginPage(driver)
    email = "testautomation123@test.com"
    password = "tester@123"

    logout_user.login_page()
    logout_user.enter_email(email)
    logout_user.enter_password(password)
    logout_user.click_login_btn()
    logout_user.click_logout_btn()

    assert "Login to your account" in driver.page_source, "user is not logged out"

