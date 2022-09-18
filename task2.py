import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects1.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    s = int(((browser.find_element(By.ID, 'num1')).text))+int(((browser.find_element(By.ID, 'num2')).text))
    print(s)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(s))

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(10)
    browser.quit()

