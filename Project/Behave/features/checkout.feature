Feature: Checkout

  @regression
  Scenario: FIRST_PRODUCT_DETAIL
    Given we are in the "Login2" screen
    When we has added the first items to the shopping cart
    When we tap on the cart option
    When we tap on CHECKOUT
    When We enter customer information
    When we tap the CONTINUAR button
    When we scroll to find the button "TERMINAR"
    When we tap on the TERMINAR button
    Then the message "GRACIAS POR SU ORDEN" is displayed