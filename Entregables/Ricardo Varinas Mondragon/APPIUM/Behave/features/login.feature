Feature: Login

    #@smoke
    Scenario: "Logging with valid credentials"
      Given we are at the app Swag Labs
      When  we fill the user textbox
      And   we fill the password textbox
      And   we click the login button
      Then  we should be at the "PRODUCTOS" screen


