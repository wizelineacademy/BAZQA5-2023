Feature: Buy Car

  Background:
      Given we are at the app Swag Labs
      When  we fill the user textbox
      And   we fill the password textbox
      And   we click the login button
      Then  we should be at the "PRODUCTOS" screen

    @smoke
    Scenario: "Buy products in the cart"
      Given we add two items in the cart
      When  we tap on the card icon
      And   we tap on the option "CHECKOUT"
      And   we add the personal info
      And   we tap on "CONTINUAR"
      And   we tap on "TERMINAR"
      Then  we validate that the thankyu page message succesfull