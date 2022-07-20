import pytest
from _pytest import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)

    but_element = browser.find_element(By.CSS_SELECTOR, 'form.add-to-basket button')

    assert but_element is not None, print('Кнопка отсутствует')
