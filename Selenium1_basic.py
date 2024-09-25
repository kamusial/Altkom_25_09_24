from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import Keys

driver = webdriver.Chrome()     # Firefox, Edge

time.sleep(2)
driver.get('https://google.com')
time.sleep(2)
print(f'Nazwa strony: {driver.title}')
time.sleep(2)

button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
time.sleep(2)

search_field = driver.find_element('id', 'APjFqb')
search_field.send_keys('Jak sie skonczyla powodz we Wroclawiu w 2024?')
time.sleep(2)
search_field.send_keys(Keys.ENTER)

# search_button = driver.find_element('name', 'btnK')
# search_button.click()
time.sleep(2)

driver.get_screenshot_as_file('screenshot.png')

driver.quit()