from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math

# Определение функции для решения математической задачи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открытие страницы
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидание, пока цена дома не станет равной $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решение математической задачи
    x_value = browser.find_element(By.ID, "input_value").text
    result = calc(x_value)

    # Ввод ответа в поле ввода
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отправка ответа
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получение результата
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    answer = alert_text.split(": ")[-1]
    print(answer)

finally:
    browser.quit()
