def take_screenshot(driver, name="screenshot"):
    path = "reports/"+ name +".png"
    driver.save_screenshot(path)
    print(f"Screenshot saved to: {path}")
