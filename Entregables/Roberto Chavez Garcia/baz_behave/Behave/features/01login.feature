Feature: Log In


  @regression
  Scenario: Log in
    Given we are in the LOGIN screen
    When we fill the user label
    And we fill the password label
    And we tap the LOGIN button
    Then we has loggin correctly we are in the Products screen

