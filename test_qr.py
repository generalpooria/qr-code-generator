from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

assert "QR Code Generator" in driver.title

input_box = driver.find_element(By.ID, "dataInput")
input_box.send_keys("Test QR Code")

generate_btn = driver.find_element(By.ID, "generateBtn")
generate_btn.click()

time.sleep(5)

qr_container = driver.find_element(By.ID, "qrContainer")
img = qr_container.find_element(By.TAG_NAME, "img")
assert img is not None

print("QR Code generated successfully.")
driver.save_screenshot("qr_code_test.png")
driver.quit()
