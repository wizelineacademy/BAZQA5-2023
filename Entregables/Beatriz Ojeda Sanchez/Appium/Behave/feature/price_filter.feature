Feature SORF_PRICE_TO_HIGHEST

  @regression
  Scenario: Sorf price to hieghest
    Given you are in the "Productos" screen
    When you select filter icon
    And you select the option low to high
    And scroll on the screen
    Then you validate the product with the highest price