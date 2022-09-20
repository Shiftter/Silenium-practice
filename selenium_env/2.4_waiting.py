from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    button = browser.find_element(By.ID,'verify')
    button.click()
    message = browser.find_element(By.ID,'verify_message')
    assert "successful" in message.text
finally:
    time.sleep(10)
    browser.quit()