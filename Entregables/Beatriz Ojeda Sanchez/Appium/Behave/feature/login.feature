Feature: LOGIN_APP

  @regression
  Scenario: Login app

    Given you are in the "LOGIN" screen
    When you fill the "Usuario" label
    And you fill the "Contraseña" label
    And you tap the "LOGIN" button
    Then you has loggin correctly we are in the "Productos" screen