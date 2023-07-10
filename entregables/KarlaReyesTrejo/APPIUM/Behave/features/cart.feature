Feature: ADD CART
  @regresion
  Scenario: ADD CART

    Given we are inside the app
    When add first product
    When validate in the cart
    Then validate product name and price
