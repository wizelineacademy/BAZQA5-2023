Feature: Log In
    @smoke
    @regresion
    Scenario: LOGIN
    Given we are on the home screen
        When enter user
        When enter password
        When we click the button
        Then we enter the app "SWAGLABS"


