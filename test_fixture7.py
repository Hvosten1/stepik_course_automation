import pytest
from _pytest import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

answer = math.log(int(time.time()))
links = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
]

@pytest.mark.parametrize('link', links)
class TestAnswer:
    mes = ''
    def  test_open_and_answer(self, link):
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            answ_element = browser.find_element(By.CSS_SELECTOR, 'div.quiz-component.ember-view textarea')
            answ_element.send_keys(answer)

            sub_element = browser.find_element(By.CSS_SELECTOR, 'div.attempt__actions button')
            sub_element.click()

            WebDriverWait(browser,5).until(EC.visibility_of_element_located('div.smart-hints.ember-view.lesson__hint p').text)

            mes_element = browser.find_element(By.CSS_SELECTOR,'div.smart-hints.ember-view.lesson__hint p')
            mes = mes_element.text

            assert mes == 'Correct!' , print(mes)



        finally:
            time.sleep(10)
            browser.quit()


if __name__ == '__main__':
    unittest.main()


@pytest.mark.skip
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.skip
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")