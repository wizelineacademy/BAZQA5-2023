Feature: PRODUCT_DETAIL

    @Regresion
    Scenario: FIRST_PRODUCT_DETAIL
    Given we are in the LOGIN screen 3
    When we tap on the first product to see the detail
    When we tap on the card icon
    Then we validate that the product title on the description is correct
    Then we validate that the product price on the description is correct