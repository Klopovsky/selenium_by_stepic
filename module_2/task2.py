import math
import time

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
    driver = Firefox(service=service, options=options)
    return driver


def go_task(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(1)
    img = driver.find_element(By.ID, "treasure")
    value = img.get_attribute("valuex")
    driver.find_element(By.ID, 'answer').send_keys(calc(value))
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task('http://suninjuly.github.io/get_attribute.html')