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
@pytest.mark.skip()
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

@pytest.mark.xfail(reason='Not implemented yet')
def test2():
    assert 3 == 5

@pytest.mark.skip(reason='Not implemented yet')
def test3():
    assert 3 == 6

@pytest.mark.skipif(len('piesekk') == 6, reason='bo piesek')
def test4():
    assert 3 == 6

@pytest.mark.filterwarnings("ignore:This is a deprecation warning")
def test_deprecated_feature():
    import warnings
    warnings.warn("This is a deprecation warning", DeprecationWarning)
    assert True

import sys
@pytest.mark.skipif(sys.platform == 'win32', reason=' pomijane na Windows')
def test5():
    assert 3 == 4



# PyTest monitoruje, czy funkcja divide(1, 0) wywoła błąd ZeroDivisionError. Jeśli nie zostanie wywołany, test zakończy się niepowodzeniem.
def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
