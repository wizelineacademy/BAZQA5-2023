Feature: ADD_THE-FIRST_PRODUCT_TO_THE_CAR

  @regression
  Scenario: ADD_THE-FIRST_PRODUCT_TO_THE_CAR
    Given we are in the "Productos" screen
    When we tap on "Añadir a carrito" from the first item
    And we tap on the car icon
    Then we validate that the product title is correct
    And we validate that the product price is correct