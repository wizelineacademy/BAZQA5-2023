Feature: PRODUCT_DETAIL

  @regression
  Scenario: Product details
    Given you are in the "Productos" screen
    When you tap on the first product to see the detail
    Then you validate the header is displayed
    And you validate that the product title on the description is correct
    And you validate that the product price on the description is correct