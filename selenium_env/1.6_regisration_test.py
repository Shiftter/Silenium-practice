import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    first = browser.find_element(By.CSS_SELECTOR,'.first_class :required')
    first.send_keys('text')
    second = browser.find_element(By.XPATH,"//div/*[@class='form-control second' and @required]")
    second.send_keys('text')
    third = browser.find_element(By.CSS_SELECTOR,'.form-control.third')
    third.send_keys('text')
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    time.sleep(0.1)
    text = browser.find_element(By.TAG_NAME,'h1')
    print(type(text))
    assert text.text == "Congratulations! You have successfully registered!"
finally:
    time.sleep(5)
    browser.quit()