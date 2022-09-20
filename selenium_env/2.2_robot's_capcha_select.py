from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    x = browser.find_element(By.ID,'num1')
    y = browser.find_element(By.ID,'num2')
    select = Select(browser.find_element(By.ID,'dropdown'))
    select.select_by_value(str(int(x.text)+int(y.text)))
    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()