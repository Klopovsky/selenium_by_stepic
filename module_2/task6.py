import os
import time
import math

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def get_driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.page_load_strategy = 'eager'
    driver = Firefox(service=service, options=options)
    return driver


def go_task(url):
    driver = get_driver()
    driver.get(url)
    driver.find_element(By.TAG_NAME, 'button').click()
    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(1)
    number = driver.find_element(By.ID, 'input_value').text
    driver.find_element(By.ID, 'answer').send_keys(calc(number))
    driver.find_element(By.TAG_NAME, 'button').click()

    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task('http://suninjuly.github.io/alert_accept.html')
