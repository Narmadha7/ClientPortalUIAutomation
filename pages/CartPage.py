import time

from selenium.webdriver.common.by import By
from pages.PaymentPage import PaymentPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[text()='Checkout']")


    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(4)
        payment = PaymentPage(self.driver)
        return payment