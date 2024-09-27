from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
time.sleep(2)
driver.find_element(By.ID, 'accept-choices').click()
time.sleep(2)

# ................jak obsłużyć przycisk, który może, ale nie musi się pojawić

# driver = webdriver.Chrome()
# driver.get("https://example.com")
# # Znajdź przyciski o określonym selektorze
# buttons = driver.find_elements(By.XPATH, "//button[@id='submit-button']")
# # Sprawdź, czy przycisk istnieje i kliknij w niego
# if buttons:
#     buttons[0].click()
#     print("Przycisk został kliknięty.")
# else:
#     print("Przycisk nie istnieje.")

# try:
#     # Próba znalezienia i kliknięcia przycisku
#     button = driver.find_element(By.XPATH, "//button[@id='submit-button']")
#     button.click()
#     print("Przycisk został kliknięty.")
# except NoSuchElementException:
#     print("Przycisk nie istnieje.")



# ............ kliknąć osobno w menu i w HTML tutorial
# menu = driver.find_element(By.ID, 'navbtn_tutorials')
# menu.click()
# time.sleep(2)
# HTMLtutorial = driver.find_element(By.XPATH, '//*[@id="tutorials_html_css_links_list"]/div[1]/a[2]')
# menu.click()
# time.sleep(2)

menu = driver.find_element(By.ID, 'navbtn_tutorials')
HTMLtutorial = driver.find_element(By.XPATH, '//*[@id="tutorials_html_css_links_list"]/div[1]/a[2]')

