import os
import time

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, r'../files/file.txt')


def get_driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.page_load_strategy = 'eager'
    driver = Firefox(service=service, options=options)
    return driver


def go_task(url, file):
    driver = get_driver()
    driver.get(url)
    driver.find_element(By.NAME, 'firstname').send_keys('zeka')
    driver.find_element(By.NAME, 'lastname').send_keys('bobs')
    driver.find_element(By.NAME, 'email').send_keys('zeka@bobs.com')
    driver.find_element(By.ID, 'file').send_keys(file)
    driver.find_element(By.TAG_NAME, 'button').click()

    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task('http://suninjuly.github.io/file_input.html', file_path)
