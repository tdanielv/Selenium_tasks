import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/math.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = int(x.text)
    a = calc(x)
    print(a)
    ans = browser.find_element(By.TAG_NAME, 'input')
    ans.send_keys(a)

    button = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    button.click()

    button = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    button.click()

    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()
    time.sleep(1)


finally:
    time.sleep(11111)
    browser.quit()

