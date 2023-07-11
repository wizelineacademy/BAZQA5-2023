Feature: Make a purchase

  @regression
  Scenario: Complete purchase
    Given we are in the "Productos" screen
    When we has added the first items to the shopping cart
    And we tap on the cart option
    And we tap on CHECKOUT
    And We enter customer information
    And we tap the CONTINUAR button
    And we scroll to find the button "TERMINAR"
    And we tap on the TERMINAR button
    Then  the message "GRACIAS POR SU ORDEN" is displayed