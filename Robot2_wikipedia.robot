*** Settings ***
Library    SeleniumLibrary
test setup  on start
test teardown    in the end
suite setup    # na początku suity - zestawu testów
suite teardown  # na końcu suity

*** Variables ***
${wikipedia login}    RobotTests
${wikipedia correct password}    RobotFramework
${wikipedia wrong password}    1234
${error message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
on start
    Open Browser    https://pl.wikipedia.org/     chrome    #executable_path=sciezka do sterownika
    maximize browser window

in the end
    capture page screenshot    screens/my screen-{index}.png
    close browser


Log in wikipedia
    [Arguments]    ${login}    ${password}

#    Click element    pt-login-2
    Click element    id:pt-login-2
    input text    id:wpName1    ${login}
    input password    id:wpPassword1    ${password}
    Select Checkbox    id:wpRemember
    Wait Until Element Is Visible    wpLoginAttempt    3
    click button    wpLoginAttempt
    sleep    2

*** Test Cases ***
Correct log in
    Log in wikipedia    ${wikipedia login}    ${wikipedia correct password}
    element should not be visible    id:pt-login-2


Incrrect log in
    Log in wikipedia    Kamil    Piesek
    ${my error message}   Get Text    xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    log    Przechwycona wiadomość: ${my error message}
    Should Be Equal   ${my error message}     ${error message}
    log to console    Przechwycona wiadomość: ${my error message}