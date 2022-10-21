import time
import math

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def get_driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    #options.page_load_strategy = 'eager'
    driver = Firefox(service=service, options=options)
    return driver


def go_task(url):
    driver = get_driver()
    driver.get(url)
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    submit = driver.find_element(By.ID, 'solve')
    driver.execute_script('return arguments[0].scrollIntoView(true);', submit)
    result = calc(driver.find_element(By.ID, 'input_value').text)
    driver.find_element(By.ID, 'answer').send_keys(str(result))
    submit.click()
    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task('http://suninjuly.github.io/explicit_wait2.html')
