import json
import time

import pytest

from pages.LoginPage import LoginPage

data_file_path = "C://Users//Narmukishore14//PycharmProjects//ClientPortalUIAutomation//data//valid_data.json"
with open(data_file_path) as f:
    testdata = json.load(f)
    data_list = testdata["data"]

@pytest.mark.parametrize("data_items",data_list)
def test_payment(browserInstance,data_items):
    driver = browserInstance
    login_page = LoginPage(driver)
    login_page.login()
    login_page.top_text()
    login_page.validate_icons()
    login_page.validate_page_texts_and_ui()
    login_page.email_label_check()
    login_page.password_label_check()
    login_page.valid_email_check(data_items["user_email"])
    login_page.valid_password_check(data_items["user_password"])
    login_page.validate_forgot_pass()
    login_page.validate_register_link()
    homepage = login_page.submit_check()

    assert "dash" in driver.current_url

    homepage.add_product_to_cart(data_items["product_name"])
    time.sleep(4)
    cartpage = homepage.click_add_to_cart()
    time.sleep(4)

    assert "cart" in driver.current_url

    payment = cartpage.click_checkout_button()
    success = payment.enter_ship_info(data_items["country_name"])
    success.validate_success_msg()
