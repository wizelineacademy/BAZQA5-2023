Feature: Sort products from lowest to highest price

  @regression
  Scenario: products from lowest to highest price
    Given we have been logged in app
    When we select filter icon
    And we select the option price low to high
    And scroll on the screen
    Then we validate the order products with the highest price
