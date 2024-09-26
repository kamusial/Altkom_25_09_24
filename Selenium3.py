from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Selenium2 import make_screenshot
from selenium.webdriver.support import expected_conditions as excon

def wait_for_id(element_id):
    timeout = 5
    timeout_message = f'Element {element_id} nie pojawil sie przez {timeout} sekund'
    lokalizator = (By.ID, element_id)
    znaleziono = excon.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)
#    return WebDriverWait(driver, timeout=5).until(excon.visibility_of_element_located((By.ID, element_id)), timeout_message)

print('Selenium3 is now running')
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)

try:
    login_button = wait_for_id('login-buttonN')
except:
    print('Nie znaleziono')
    raise
else:
    print('znaleziono')
finally:
    print('Dalsza część programu')
    make_screenshot(driver)
    driver.quit()