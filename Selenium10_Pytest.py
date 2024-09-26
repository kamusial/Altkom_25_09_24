import time

import pytest
from selenium import webdriver
from Selenium6_POM import LoginPage
from Selenium2 import make_screenshot
from selenium.webdriver.common.by import By
from time import sleep

# id="inventory_container"

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.parametrize('user, password, url', test_data)
def test_login_page(user, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username(user)
    page.enter_password(password)
    page.click_login()
    sleep(2)
    try:
        assert page.get_page_url() == url
    except AssertionError:
        print('Asercja nie przeszła')
        raise
    else:
        print('Asercja przeszła')
    finally:
        print('Po asercji')
        page.make_screenshot('SKRIIIN')
        page.clear_and_close()
