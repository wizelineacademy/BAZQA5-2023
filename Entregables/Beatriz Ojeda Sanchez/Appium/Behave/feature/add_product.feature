Feature: ADD_PRODUCT_CAR

@regression
  Scenario: Add product car
    Given you are in the "Productos" screen
    When you tap on "Añadir a carrito" from the first item
    And you tap on the car icon
    Then you validate that the product title is correct
    And you validate that the product price is correct