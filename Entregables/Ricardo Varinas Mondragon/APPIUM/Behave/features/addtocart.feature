Feature: Add to car

  Background:
      Given we are at the app Swag Labs
      When  we fill the user textbox
      And   we fill the password textbox
      And   we click the login button
      Then  we should be at the "PRODUCTOS" screen

    @smoke
    Scenario: "Add product to cart to validate item"
      Given we are in the screen of the first item
      When   we tap on "AÑADIR A CARRITO"
      And   we tap on the card icon
      Then  we validate that the product title, price and description is correct

