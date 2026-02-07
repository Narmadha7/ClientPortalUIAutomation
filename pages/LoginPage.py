import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.ID, "userEmail")
        self.password = (By.ID, "userPassword")
        self.submit = (By.ID, "login")
        self.label_email = (By.XPATH, "//label[@for='email']")
        self.label_password = (By.XPATH, "//label[@for='password']")
        self.mail_top_text = (By.XPATH, "//div[@class='top-tab']/span[1]/a")
        self.top_icons = (By.CSS_SELECTOR, ".fa")
        self.small_text = (By.XPATH, "//h3[text()='We Make Your Shopping Simple']")
        self.title_text = (By.XPATH, "(//h1[@class='title'])[1]")
        self.blink_text = (By.CSS_SELECTOR, ".blink_me")
        self.login_title = (By.CSS_SELECTOR, ".login-title")
        # self.page_title = ()
        self.forgot_pass = (By.XPATH, "//a[text()='Forgot password?']")
        self.register_link = (By.CSS_SELECTOR, ".text-reset")
        self.toast_msg = (By.CSS_SELECTOR, "#toast-container")
        self.email_valid_error = (By.XPATH, "//div[contains(text(), '*Email is required')]")
        self.password_valid_error = (By.XPATH, "//div[contains(text(), '*Password is required')]")
        self.body = driver.find_element(By.TAG_NAME, "body")

    def email_label_check(self):
        return self.driver.find_element(*self.label_email).text.title()

    def is_email_displayed(self):
        return self.driver.find_element(*self.email).is_displayed()

    def get_email_placeholder(self):
        return self.driver.find_element(*self.email).get_attribute("placeholder")

    def enter_email(self, email_input):
        self.driver.find_element(*self.email).send_keys(email_input)

    def empty_email_error(self):
        return self.driver.find_element(*self.email_valid_error).text

    def empty_password_error(self):
        return self.driver.find_element(*self.password_valid_error).text

    def password_label_check(self):
        return self.driver.find_element(*self.label_password).text.title()

    def is_password_displayed(self):
        return self.driver.find_element(*self.password).is_displayed()

    def get_password_placeholder(self):
        return self.driver.find_element(*self.password).get_attribute("placeholder")

    def enter_password(self, pass_input):
        password = self.driver.find_element(*self.password)
        password.send_keys(pass_input)

    def is_button_enabled(self):
        return self.driver.find_element(*self.submit).is_enabled()

    def login_button_text(self):
        return self.driver.find_element(*self.submit).get_attribute("value")

    def submit_click(self):
        self.driver.find_element(*self.submit).click()
        time.sleep(3)
        # homepage = HomePage(self.driver)
        # return homepage

    # def validate_toast_msg(self):
    #     return self.driver.find_element(*self.toast_msg).text

    def is_top_text_displayed(self):
        return self.driver.find_element(*self.mail_top_text).is_displayed()

    def validate_icons(self):
        icons = self.driver.find_elements(*self.top_icons)
        assert len(icons) >= 4

        for i, icon in enumerate(icons[:4]):
            href = icon.find_element(By.XPATH, "..").get_attribute("href")
            print(f"{icon.get_attribute('class')} = {href}")

    def validate_small_text(self):
        return self.driver.find_element(*self.small_text).text

    def validate_title_text(self):
        return self.driver.find_element(*self.title_text).text

    def validate_blink_text(self):
        return self.driver.find_element(*self.blink_text).text

    def validate_login_text(self):
        return self.driver.find_element(*self.login_title).text

    def forgot_password_id_displayed(self):
        return self.driver.find_element(*self.forgot_pass).is_displayed()

    def validate_forgot_pass(self):
        return self.driver.find_element(*self.forgot_pass).text

    def register_link_id_displayed(self):
        return self.driver.find_element(*self.register_link).is_displayed()

    def validate_register_link(self):
        return self.driver.find_element(*self.register_link).text

    def verify_login_title(self):
        return self.driver.title

    def verify_current_page(self):
        return self.driver.current_url

    def click_forgot_pass(self):
        self.driver.find_element(*self.forgot_pass).click()
        time.sleep(2)

    def click_register_link(self):
        self.driver.find_element(*self.register_link).click()
        time.sleep(2)

    def navigate_using_keyboard(self, email):
        for _ in range(6):
            self.body.send_keys(Keys.TAB)
            time.sleep(3)
            self.body.send_keys("email.com")
            time.sleep(5)

    # def validate_toast_msgs(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 5)  # Increase timeout to be safe
    #         toast = wait.until(EC.presence_of_element_located(*self.toast_msg))
    #         return toast.text
    #     except:
    #         return "Toast not found"

    def validate_toast_msg(self):
        try:
            toast_locator = (By.CSS_SELECTOR, "#toast-container")
            wait = WebDriverWait(self.driver, 5)
            toast = wait.until(EC.visibility_of_element_located(toast_locator))
            return toast.text
        except Exception as e:
            print("Toast not found or disappeared too fast:", e)
            return ""

