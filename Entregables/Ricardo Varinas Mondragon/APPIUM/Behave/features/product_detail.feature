Feature: Product Detail

    Background:
      Given we are at the app Swag Labs
      When  we fill the user textbox
      And   we fill the password textbox
      And   we click the login button
      Then  we should be at the "PRODUCTOS" screen

    @smoke
    Scenario: "Existing product detail on product page"
      Given we are in te "PRODUCTOS" screen
      When  we tap on the first item
      Then  we validate the name and price of the product

