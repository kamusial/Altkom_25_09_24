*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipedia login}    RobotTests
${wikipedia password}    RobotFramework
*** Keywords ***


*** Test Cases ***
Test 1
    Open Browser    https://pl.wikipedia.org/     chrome    #executable_path=sciezka do sterownika
    maximize browser window
#    Click element    pt-login-2
    Click element    id:pt-login-2
    input text    id:wpName1    ${wikipedia login}
    input password    id:wpPassword1    ${wikipedia password}
    Select Checkbox    id:wpRemember
    sleep    2
    click button    wpLoginAttempt
    sleep    2
    capture page screenshot    screens/my screen-{index}.png
    close browser
