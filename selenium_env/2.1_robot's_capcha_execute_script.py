from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


try:
    browser = webdriver.Chrome(options=options)
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID,'input_value')
    input = browser.find_element(By.ID,'answer')
    input.send_keys(calc(x.text))
    checkbox = browser.find_element(By.ID,'robotCheckbox')
    radio = browser.find_element(By.ID,'robotsRule')
    button = browser.find_element(By.CLASS_NAME,'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)
    radio.click()
    checkbox.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()