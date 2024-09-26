from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

def make_screenshot(driver):
#     driver.get_screenshot_as_file('screen2.png')
    teraz = datetime.datetime.now()
    file_name = teraz.strftime('C:\\Users\\Student\\Desktop\\Altkom_25_09_24\\screens\\screenshot%H-%M-%S.png')
    driver.get_screenshot_as_file(file_name)


if __name__ == '__main__':   # wykonaj tylko, gdy plik bezporednio uruchomiony (nie zaimportowany)
    print('Selenium2 is now running')

    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    print('Nazwa strony', driver.title)
    time.sleep(3)

    try:
        username_field = driver.find_element(By.ID, 'user-nameQ')
    except:
        username_field = driver.find_element(By.XPATH, '// *[ @ id = "user-name"]')
        print('nie znaleziono po ID, znaleziono po XPATH')

    username_field.clear()
    username_field.send_keys('standard_user')
    time.sleep(3)

    try:
        password_field = driver.find_element('id', 'password')
    except NoSuchElementException:
        make_screenshot(driver)
        print('nie znaleziono pola z haslem')
        raise

    password_field.clear()
    password_field.send_keys('secret_sauce')
    time.sleep(3)

    login_button = driver.find_element(By.NAME, 'login-button')
    if not login_button.get_attribute('disabled'):
        login_button.click()
        print('klikniety')
    else:
        print('nie kliknieto')

    time.sleep(3)
    make_screenshot(driver)

    driver.quit()