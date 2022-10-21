import math
import time

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import Select


def get_driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    driver = Firefox(service=service, options=options)
    return driver


def go_task(url):
    driver = get_driver()
    driver.get(url)
    result = str(int(driver.find_element(By.ID, 'num1').text) + int(driver.find_element(By.ID, 'num2').text))
    drowdown = Select(driver.find_element(By.TAG_NAME, 'select'))
    drowdown.select_by_visible_text(result)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task('http://suninjuly.github.io/selects1.html')
