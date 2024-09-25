import time

from selenium import webdriver
from Selenium6_POM import LoginPage
from Selenium2 import make_screenshot
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.print_page_info()
page.enter_username('Kamil')


page.close()

