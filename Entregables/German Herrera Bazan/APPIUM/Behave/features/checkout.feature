Feature: Make a purchase

Background:
      Given login

      @smoke
      Scenario: Complete purchase
        Given the user has added multiple items to the shopping cart
        When the user selects the cart option
        And the purchase confirmation screen is displayed
        And customer data is entered
        And I tap the continue button
        And we scroll to find the button
        And we tap on the terminar button
        Then you should be redirected to the order processed screen