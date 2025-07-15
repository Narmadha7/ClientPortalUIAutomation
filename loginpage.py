import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

assert "client" in driver.current_url
print("Title is:", driver.title)

mail_text = driver.find_element(By.XPATH, "//div[@class='top-tab']/span[1]/a")
mail_text.is_displayed()
print(mail_text.text)

icons = driver.find_elements(By.CSS_SELECTOR, ".fa")
assert len(icons)>=4
print("Icons present is:", len(icons))

for i, icon in enumerate(icons[:4]):
    href = icon.find_element(By.XPATH, "..").get_attribute("href")
    print(f"{icon.get_attribute('class')} = {href}")

small_text = driver.find_element(By.XPATH, "//h3[text()='We Make Your Shopping Simple']").text
print(small_text)
title_text = driver.find_element(By.XPATH, "(//h1[@class='title'])[1]").text
print(title_text)
blink_text = driver.find_element(By.CSS_SELECTOR, ".blink_me").text
print(blink_text)

Login_title = driver.find_element(By.CSS_SELECTOR, ".login-title")
print(Login_title.text)

forgot_pass = driver.find_element(By.XPATH, "//a[text()='Forgot password?']")
forgot_pass.is_displayed()
assert forgot_pass.text in driver.page_source

register_link = driver.find_element(By.CSS_SELECTOR, ".login-wrapper p")
register_link.is_displayed()
print(register_link.text)

label_email = driver.find_element(By.XPATH, "//label[@for='email']")
assert label_email.text.title() == "Email"

email = driver.find_element(By.ID, "userEmail")
assert email.is_displayed()
print("Placeholder Email:", email.get_attribute("placeholder"))
email.send_keys("brainandbeauty@test.com")
time.sleep(2)

label_pass = driver.find_element(By.XPATH, "//label[@for='password']")
assert label_pass.text.title() == "Password"

password = driver.find_element(By.ID, "userPassword")
assert password.is_displayed()
print("Placeholder password:", password.get_attribute("placeholder"))
password.send_keys("Brain@123")
time.sleep(2)
submit_button = driver.find_element(By.ID, "login")
submit_button.is_enabled()
submit_button.click()

time.sleep(3)
assert "dash" in driver.current_url

items_list = driver.find_elements(By.CSS_SELECTOR, ".mb-3")

for item in items_list:
    name = item.find_element(By.CSS_SELECTOR, "b").text
    if name == "ZARA COAT 3":
        item.find_element(By.CSS_SELECTOR, "button.w-10").click()
        print("Item found!!")
        break

time.sleep(4)

driver.find_element(By.XPATH, "(//i[@class='fa fa-shopping-cart'])[1]").click()

time.sleep(4)

driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()


time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ta-results")))

# Select "India"
countries = driver.find_elements(By.CSS_SELECTOR, ".ta-results button")
for country in countries:
    if country.text == "India":
        country.click()
        break

driver.find_element(By.XPATH, "//div[@class='actions']/a").click()
time.sleep(4)

print(driver.find_element(By.CSS_SELECTOR, ".hero-primary").text)

time.sleep(4)

