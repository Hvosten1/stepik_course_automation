from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestUnit(unittest.TestCase):

    def test_uni1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            form1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.first_class input")
            form1.send_keys("Hi1")

            form2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
            form2.send_keys("Hi3")

            form3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input")
            form3.send_keys("Hi2")

            form4 = browser.find_element(By.CSS_SELECTOR, "div.second_block div.form-group.first_class input")
            form4.send_keys("Hihi")

            form5 = browser.find_element(By.CSS_SELECTOR, "div.second_block div.form-group.second_class input")
            form5.send_keys("Hihi")

            time.sleep(5)

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text, "Registration failed"

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_uni2(self):

            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            form1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.first_class input")
            form1.send_keys("Hi1")

            form2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
            form2.send_keys("Hi3")

            form3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input")
            form3.send_keys("Hi2")

            form4 = browser.find_element(By.CSS_SELECTOR, "div.second_block div.form-group.first_class input")
            form4.send_keys("Hihi")

            form5 = browser.find_element(By.CSS_SELECTOR, "div.second_block div.form-group.second_class input")
            form5.send_keys("Hihi")

            time.sleep(5)

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text, "Registration failed"


            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
