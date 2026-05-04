import random
from pages.NewUserLogin import NewUserLogin
from pages.account_info import AccountInfoPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_signup_flow(setup):
    driver = setup
    driver.get("https://automationexercise.com/")
    signup = NewUserLogin(driver)
    name = "Tester1"
    email = f"user{random.randint(1000,9999)}@test.com"

    signup.click_login()
    signup.enter_name(name)
    signup.enter_email(email)
    signup.click_signup()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))
    assert "Enter Account Information" in driver.page_source
    print(driver.current_url)


    account = AccountInfoPage(driver)

    account.select_title("mrs")
    account.enter_password("test@1234")
    account.select_day("10")
    account.select_month("11")
    account.select_year("1998")
    account.click_newsletter()
    account.click_spcl_offers()

    account.enter_first_name("Automation")
    account.enter_last_name("Tester")
    account.enter_company_name("TestCompany")
    account.enter_add("Noida")
    account.select_country_name("India")
    account.enter_state("Uttar Pradesh")
    account.enter_city("Noida")
    account.enter_zipcode("122032")
    account.enter_mob_no("9090909090")
    account.click_create_btn()
    print(driver.current_url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))
    assert driver.find_element(By.XPATH, "//h2[@data-qa='account-created']").is_displayed()
    print(driver.current_url)