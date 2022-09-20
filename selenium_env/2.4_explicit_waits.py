from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    browser = webdriver.Chrome(options=options)
    link = "http://suninjuly.github.io/wait2.html"
    browser.get(link)
    button = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.ID,'verify')))
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
finally:
    time.sleep(10)
    browser.quit()