*** Settings ***
Documentation        testcases3
Library         OperatingSystem
*** Keywords ***

*** Variables ***
${var}    MY VAR

*** Test Cases ***
TEST
    [Tags]    Demo2
    Log    ${var}
