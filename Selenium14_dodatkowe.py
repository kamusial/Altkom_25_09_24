# text elementu
heading = driver.find_element(By.TAG_NAME, "h1")
print(heading.text)

# wartość danego atrybutu
link = driver.find_element(By.LINK_TEXT, "Click here")
href_value = link.get_attribute("href")
print(href_value)

# czy element jest widoczny na stronie
element = driver.find_element(By.ID, "hidden-element")
print(element.is_displayed())

# czy element jest aktywny
button = driver.find_element(By.ID, "submit-button")
print(button.is_enabled())

# czy zaznaczony
checkbox = driver.find_element(By.ID, "agree")
print(checkbox.is_selected())

# wymiary okna
driver.maximize_window()
driver.minimize_window()

##### praca z listami rozwijanymi
from selenium.webdriver.support.ui import Select
# znalezienie elementu listy rozwijanej
dropdown = Select(driver.find_element(By.ID, "dropdown-id"))
# wybieranie opcji po widocznej nazwie
dropdown.select_by_visible_text("Option 1")
# wybieranie opcji po wartości atrybutu "value"
dropdown.select_by_value("value1")
# wybieranie opcji po indeksie
dropdown.select_by_index(2)
# pobranie wszystkich dostępnych opcji
all_options = dropdown.options
for option in all_options:
    print(option.text)

##### praca z checkboxami
checkbox = driver.find_element(By.ID, "checkbox-id")
# zaznaczenie checkboxa, jeśli nie jest zaznaczony i odwrotnie
if not checkbox.is_selected():
    checkbox.click()    # zaznacz

if checkbox.is_selected():
    checkbox.click()    # odznacz

##### praca  przyciskami radiowymi (radio buttons)
radio_button = driver.find_element(By.ID, "radio-button-id")
if not radio_button.is_selected():
    radio_button.click()

##### praca z ramkami
driver.switch_to.frame("frame-id")
driver.switch_to.default_content()    # do pierwszej / głównej
# przełącz do ramki wg indeksu
driver.switch_to.frame(0)


###### praca z oknami JavaScript (alert, confirm, prompt)
# akceptowanie okna alert
alert = driver.switch_to.alert
print(alert.text)  # Wyświetlenie tekstu alertu
alert.accept()     # Akceptowanie alertu

# anulowanie okna confirm
confirm = driver.switch_to.alert
print(confirm.text)
confirm.dismiss()  # Anulowanie (kliknięcie "Anuluj")

# wprowadzenie tekstu
prompt = driver.switch_to.alert
prompt.send_keys("Tekst do wpisania w oknie prompt")
prompt.accept()

###### pobieranie atrybutów i właściwości CSS
# pobieranie wartości atrybutu HTML
element = driver.find_element(By.ID, "example-element")
attribute_value = element.get_attribute("href")
print(f"Atrybut 'href' elementu: {attribute_value}")

# pobieranie właściwości CSS
css_value = element.value_of_css_property("color")
print(f"Wartość CSS 'color': {css_value}")


###### praca z tabelami
# znalezienie wartości w tabeli
cell_value = driver.find_element(By.XPATH, "//table[@id='example-table']/tbody/tr[2]/td[3]").text
print(f"Wartość z drugiego wiersza, trzeciej kolumny: {cell_value}")

# pobieranie wszystkich danych
rows = driver.find_elements(By.XPATH, "//table[@id='example-table']/tbody/tr")

for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    row_data = [col.text for col in columns]
    print(row_data)


# wykoniwanie skryptów JavaScript
value = driver.execute_script("return document.title;")
print(f"Tytuł strony: {value}")

# przewijanie strony
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#### sprawdzanie obecności elementu na stronie
from selenium.common.exceptions import NoSuchElementException

def element_exists(by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False

if element_exists(By.ID, "non-existent-element"):
    print("Element istnieje.")
else:
    print("Element nie istnieje.")