import time

from selenium import webdriver
from Selenium6_POM import LoginPage
from Selenium2 import make_screenshot
from selenium.webdriver.common.by import By
from time import sleep

addr_after_login = 'https://www.saucedemo.com/inventory.html'
# id="inventory_container"

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.print_page_info()
page.enter_username('standard_userA')
page.enter_password('secret_sauce')
page.click_login()
sleep(2)

try:
    assert page.get_page_url() == addr_after_login
except AssertionError:
    print('Asercja nie przeszła')
    raise
else:
    print('Asercja przeszła')
finally:
    print('Po asercji')
    page.clear_and_close()


page.make_screenshot('SKRIIIN')
page.close()

