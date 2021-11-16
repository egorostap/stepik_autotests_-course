#python c:\Users\Конфетки\environments\selenium_course\lesson2_4_step8.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # говорим Selenium проверять в течение 12 секунд, пока цена не уменьшится до $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )

    button = browser.find_element(By.ID, 'book').click()     #Нажимаем на кнопку book

    x = browser.find_element_by_css_selector("span#input_value").text     # Считываем значение для переменной х
    y = calc(x)     # Считаем математическую функцию от х
    y_element = browser.find_element_by_css_selector("input#answer")
    y_element.send_keys(y)     #Вводим значение y в текстовое поле

    button = browser.find_element(By.ID, 'solve').click()       #Нажимаем на кнопку Submit

finally:
    time.sleep(5)     # ожидание чтобы визуально оценить результаты прохождения скрипта
    browser.quit()    # закрываем браузер после всех манипуляций
