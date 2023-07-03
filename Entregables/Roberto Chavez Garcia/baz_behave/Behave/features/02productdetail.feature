Feature: PRODUCT_DETAIL

  @regression
  
  Scenario: FIRST_PRODUCT_DETAIL
    Given we have been logged in app
    When we tap on the first product to see the detail
    And we validate the header is displayed
    Then we validate that the product title and price on the description is correct