import math
import time

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import Select


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
    value = calc(driver.find_element(By.ID, 'input_value').text)
    driver.find_element(By.ID, 'answer').send_keys(value)
    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    radiobutton = driver.find_element(By.ID, 'robotsRule')
    submit = driver.find_element(By.TAG_NAME, 'button')
    driver.execute_script('return arguments[0].scrollIntoView(true);', checkbox)
    checkbox.click()
    driver.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
    radiobutton.click()
    driver.execute_script('return arguments[0].scrollIntoView(true);', submit)
    submit.click()
    time.sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    go_task("https://SunInJuly.github.io/execute_script.html")
