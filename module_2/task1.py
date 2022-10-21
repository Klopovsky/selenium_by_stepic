import math
import time

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def get_driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    driver = Firefox(service=service, options=options)
    return driver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def go_task(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(1)
    number = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    driver.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    driver.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(number))
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task('https://suninjuly.github.io/math.html')