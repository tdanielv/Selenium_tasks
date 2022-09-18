import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:

    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.window(browser.window_handles[1])

    browser.find_element(By.ID, 'answer').send_keys(str(calc(int(browser.find_element(By.ID, 'input_value').text))))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(10)
    browser.quit()
