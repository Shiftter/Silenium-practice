from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    browser = webdriver.Chrome(options=options)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    browser.find_element(By.ID,'book').click()

    button = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.ID,'solve')))

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x = browser.find_element(By.ID, 'input_value')
    input = browser.find_element(By.ID,'answer')
    input.send_keys(calc(x.text))


    button.click()
finally:
    time.sleep(10)
    browser.quit()