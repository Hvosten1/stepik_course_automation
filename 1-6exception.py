import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))

button = browser.find_element(By.ID, 'book')
button.click()

x_elem = browser.find_element(By.ID, 'input_value')
x = x_elem.text

res = math.log(abs(12*math.sin(int(x))))

res_elem = browser.find_element(By.ID, 'answer')
res_elem.send_keys(res)

sub_elem = browser.find_element(By.ID, 'solve')
sub_elem.click()



time.sleep(10)
browser.quit()
