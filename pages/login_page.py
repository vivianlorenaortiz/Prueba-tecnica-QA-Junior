from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.title_module = (By.CLASS_NAME, 'title')
        self.inventory = (By.ID, 'inventory_container')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def display_inventory(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.inventory))
        return self.driver.find_element(*self.inventory).is_displayed()

    def get_title_module(self):
        return self.driver.find_element(*self.title_module).text