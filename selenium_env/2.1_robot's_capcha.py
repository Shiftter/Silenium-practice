from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

try:
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    x = browser.find_element(By.ID,'input_value')
    input = browser.find_element(By.ID,'answer')
    input.send_keys(calc(x.text))
    checkbox = browser.find_element(By.ID,'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID,'robotsRule')
    radio.click()
    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()