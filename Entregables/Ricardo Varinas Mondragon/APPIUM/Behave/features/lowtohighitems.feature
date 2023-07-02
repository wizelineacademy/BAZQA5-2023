Feature: Filter products low to high

    Background:
      Given we are at the app Swag Labs
      When  we fill the user textbox
      And   we fill the password textbox
      And   we click the login button
      Then  we should be at the "PRODUCTOS" screen

    @smoke
    Scenario: "Arrangement of products from lowest to highest price"
      Given we are in the screen of products ordered by name
      When  we tap on filter botton
      And   we select the opcion "Price(low to high)"
      Then  we validate the ordered by low to high price