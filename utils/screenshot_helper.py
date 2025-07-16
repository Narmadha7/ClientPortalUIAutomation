
import os, time

def take_screenshot(driver, name="screenshot"):
    print("📸 Screenshot function called")  # ✅ Debug line
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    folder = "reports"
    os.makedirs(folder, exist_ok=True)
    path = f"{folder}/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    print(f"✅ Screenshot saved to: {path}")
