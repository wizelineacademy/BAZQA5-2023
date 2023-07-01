Feature: ADD_PRODUCT_TO_THE_CAR

  @regression
  Scenario: ADD_THE-FIRST_PRODUCT_TO_THE_CAR
    Given we have been logged in app
    When We click on add to the cart of the first product
    And tap on the card icon
    Then We validate that the product, price and title information is correct

