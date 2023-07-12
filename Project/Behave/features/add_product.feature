Feature: ADD_THE-FIRST_PRODUCT_TO_THE_CAR

  @regression
  Scenario: ADD_THE-FIRST_PRODUCT_TO_THE_CAR
    Given we are in the "Login1" screen
    When we tap on "Añadir a carrito" from the first item
    Then we tap on the car icon
    Then we validate that the product title is correct
    Then we validate that the product price is the correct