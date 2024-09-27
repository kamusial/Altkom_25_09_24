from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
driver.maximize_window()
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

webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
time.sleep(2)

HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')
HTML_forms_attributes.click()
time.sleep(2)
tryityourself = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
tryityourself.click()
time.sleep(2)

# runbtn = driver.find_element(By.ID, 'runbtn')
# runbtn.click()
# time.sleep(2)
# otwarto w nowej karcie

currentWindowName = driver.current_window_handle
windowsNames = driver.window_handles
print(currentWindowName)
print(windowsNames)

# driver.switch_to.window(windowsNames[1])

for window in windowsNames:
    if window != currentWindowName:
        driver.switch_to.window(window)
        print(f'jesteś w nowej karcie: {driver.title}, \n{driver.current_url}')

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))
firstName = driver.find_element(By.ID, 'fname')

if firstName.is_enabled():
    firstName.clear()
    firstName.send_keys('Kamil')
else:
    print('nie da się kliknąć')

driver.close()     # zamyka aktualną kartę
driver.quit()      # zamyka przeglądarkę