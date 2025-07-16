import time

from selenium.webdriver.common.by import By
from pages.CartPage import CartPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.all_products = (By.CSS_SELECTOR, ".mb-3")
        self.product_title = (By.CSS_SELECTOR, "b")
        self.cart_button = (By.XPATH, "(//i[@class='fa fa-shopping-cart'])[1]")

    def add_product_to_cart(self, product_name):
        items_list = self.driver.find_elements(*self.all_products)

        for item in items_list:
            name = item.find_element(*self.product_title).text
            if name == product_name:
                item.find_element(By.CSS_SELECTOR, "button.w-10").click()
                print("Item found!!")
                break

        time.sleep(4)

    def click_add_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        time.sleep(4)
        cartpage = CartPage(self.driver)
        return cartpage