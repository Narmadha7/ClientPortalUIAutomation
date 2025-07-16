import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.SuccessPage import SuccessPage


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.country_text = (By.CSS_SELECTOR, "input[placeholder='Select Country']")
        self.place_order_button = (By.XPATH, "//div[@class='actions']/a")


    def enter_ship_info(self, country_name):
        self.driver.find_element(*self.country_text).send_keys(country_name)
        my_wait = WebDriverWait(self.driver, 10)
        my_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ta-results")))

        # Select "India"
        countries = self.driver.find_elements(By.CSS_SELECTOR, ".ta-results button")
        for country in countries:
            if country.text == "India":
                country.click()
                break

        self.driver.find_element(*self.place_order_button).click()
        time.sleep(4)
        success = SuccessPage(self.driver)
        return success

