Feature: Add_product_car
    @Regresion

    Scenario: Add_product_car
    Given we are in the LOGIN screen 2
    When we tap on Agregar a carrito button from the first item
    And we tap on the cart icon
    Then we validate that the product title is correct
    Then we validate that the product price is correct
