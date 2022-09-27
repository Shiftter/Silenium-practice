from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistrationSilenium(unittest.TestCase):
    def test_registration1(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        browser.get("http://suninjuly.github.io/registration1.html")
        first = browser.find_element(By.CSS_SELECTOR, '.first_class :required')
        first.send_keys('text')
        second = browser.find_element(By.CSS_SELECTOR, '.second_class :required')
        second.send_keys('text')
        third = browser.find_element(By.CSS_SELECTOR, '.third_class :required')
        third.send_keys('text')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(0.1)
        text = browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(text.text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        browser.quit()

    def test_registration2(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        browser.get("http://suninjuly.github.io/registration2.html")
        first = browser.find_element(By.CSS_SELECTOR, '.first_class :required')
        first.send_keys('text')
        second = browser.find_element(By.CSS_SELECTOR, '.second_class :required')
        second.send_keys('text')
        third = browser.find_element(By.CSS_SELECTOR, '.third_class :required')
        third.send_keys('text')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(0.1)
        text = browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(text.text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        browser.quit()

if __name__ == "__main__":
        unittest.main()