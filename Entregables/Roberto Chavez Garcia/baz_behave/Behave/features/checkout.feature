Feature: Checkout
  @Regrecion
  @Smoke
    Scenario: Allow the user to finalize the purchase of the product
    Given we are in the LOGIN screen 5
    When we add the products to the cart
    And we select the shopping cart
    And we select checkout button
    And we enter customer information
    And we press continue button
    And we scroll to find the finish button
    And we press the finish button
    Then we show purchase success screen