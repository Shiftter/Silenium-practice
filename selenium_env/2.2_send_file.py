from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


try:
    browser = webdriver.Chrome(options=options)
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first = browser.find_element(By.NAME, 'firstname')
    first.send_keys('text')
    second = browser.find_element(By.NAME, 'lastname')
    second.send_keys('text')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('text')
    input = browser.find_element(By.ID,'file')
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir,'text.txt')
    input.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()