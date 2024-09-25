# Page Object Model
import time

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_btn_name = 'login-button'

    def open(self):
        self.driver.get('http://www.saucedemo.com')

    def print_page_info(self):
        print('Nazwa strony', self.driver.title)
        print('adres:', self.driver.current_url)

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(By.NAME, self.login_button_name)
        button.click()

    def close(self):
        self.driver.quit()

    def clear_and_close(self):
        time.sleep(2)
        print('Sprzątam')
        self.driver.quit()