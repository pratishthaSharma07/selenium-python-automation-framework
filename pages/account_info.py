from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class AccountInfoPage:

    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)

       self.password = (By.ID, "password")
       self.days = (By.ID, "days")
       self.months = (By.ID, "months")
       self.years = (By.ID, "years")
       self.newsletter = (By.ID, "newsletter")
       self.spcl_offers = (By.ID, "optin")

       self.first_name = (By.ID, "first_name")
       self.last_name = (By.ID, "last_name")
       self.company_name = (By.ID, "company")
       self.address1 = (By.ID, "address1")
       self.countries = (By.ID, "country")
       self.states = (By.ID, "state")
       self.cities = (By.ID, "city")
       self.zip_codes = (By.ID, "zipcode")
       self.mob_no = (By.ID, "mobile_number")
       self.create_account = (By.XPATH, "//button[@data-qa='create-account']")

    def select_title(self, gender):
           if gender.lower() == "mr":
               locator = (By.ID, "id_gender1")
           else:
               locator = (By.ID, "id_gender2")
           self.driver.find_element(*locator).click()

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password))
        self.driver.find_element(*self.password).send_keys(password)

    def select_day(self, day):
        dropdown = Select(self.driver.find_element(*self.days))
        dropdown.select_by_value(day)

    def select_month(self, month):
        dropdown = Select(self.driver.find_element(*self.months))
        dropdown.select_by_value(month)

    def select_year(self, year):
        dropdown = Select(self.driver.find_element(*self.years))
        dropdown.select_by_value(year)
    
    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,500)")

    def click_newsletter(self):
        self.driver.find_element(*self.newsletter).click()
    def click_spcl_offers(self):
        self.driver.find_element(*self.spcl_offers).click()

    def enter_first_name(self, firstname):
        self.driver.find_element(*self.first_name).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.last_name).send_keys(lastname)
    
    def enter_company_name(self, companyname):
        self.driver.find_element(*self.company_name).send_keys(companyname)

    def enter_add(self, address):
        self.driver.find_element(*self.address1).send_keys(address)

    def select_country_name(self, country):
        dropdown = Select(self.driver.find_element(*self.countries))
        dropdown.select_by_value(country)

    def enter_state(self, state):
        self.driver.find_element(*self.states).send_keys(state)

    def enter_city(self, city):
        self.driver.find_element(*self.cities).send_keys(city)

    def enter_zipcode(self, zipcode):
        self.driver.find_element(*self.zip_codes).send_keys(zipcode)

    def enter_mob_no(self, mob_num):
        self.driver.find_element(*self.mob_no).send_keys(mob_num)

    def click_create_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.create_account))
        self.driver.find_element(*self.create_account).click()