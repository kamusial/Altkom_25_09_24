*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Test 1
    Open Browser    https://pl.wikipedia.org/     chrome    #executable_path=sciezka do sterownika
    maximize browser window

#    Click element    pt-login-2
    Click element    id:pt-login-2


    sleep    2
    close browser
