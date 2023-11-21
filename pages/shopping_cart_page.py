from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_product = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.add_product_bike = (By.ID, 'add-to-cart-sauce-labs-bike-light')
        self.cart = (By.ID, 'shopping_cart_container')
        self.checkout = (By.ID, 'checkout')
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.cancel_button = (By.ID, 'cancel')
        self.title_module = (By.CLASS_NAME, 'title')
        self.checkout_container = (By.ID, 'checkout_summary_container')
        self.total_price = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
        self.remove_one_product = (By.ID, 'remove-sauce-labs-bike-light')

    def click_add_product(self):
        self.driver.find_element(*self.add_product).click()
        self.driver.find_element(*self.add_product_bike).click()

    def click_go_to_cart(self):
        self.driver.find_element(*self.cart).click()

    def click_go_to_checkout(self):
        self.driver.find_element(*self.checkout).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def click_continue_button_checkout(self):
        self.driver.find_element(*self.continue_button).click()

    def click_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()

    def click_remove_one_product(self):
        self.driver.find_element(*self.remove_one_product).click()

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text

    def get_title_module(self):
        return self.driver.find_element(*self.title_module).text

    def display_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.checkout_container))
        return self.driver.find_element(*self.checkout_container).is_displayed()
