Feature: MAKE_A_BUY

  @regression
  Scenario: Make to buy
    Given you are in the "Productos" screen
    When you has added the first items to the shopping cart
    And you tap on the cart option
    And you tap on CHECKOUT
    And you enter customer information
    And you tap the CONTINUAR button
    And you scroll to find the button "TERMINAR"
    And you tap on the TERMINAR button
    Then  the message "GRACIAS POR SU ORDEN" is displayed