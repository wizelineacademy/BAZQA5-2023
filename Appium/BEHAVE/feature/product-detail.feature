Feature: PRODUCT_DETAIL

  @regression
  Scenario: FIRST_PRODUCT_DETAIL
    Given we are in the "Productos" screen
    When we tap on the first product to see the detail
    Then we validate that the product title on the description is correct
    And we validate that the product price on the description is correct