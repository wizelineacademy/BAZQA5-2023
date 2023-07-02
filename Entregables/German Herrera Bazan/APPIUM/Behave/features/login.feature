Feature: Log In

    @regression
    Scenario: Successful login
      Given I am in the Sauce Labs application
      When Enter my username
      And Enter my password
      And I tap the login
      Then I can see title Products


