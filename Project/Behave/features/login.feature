Feature: LOGIN

  @Smoke
  Scenario: Login_in_the_app
    Given we are in the "LOGIN" screen
    When we fill the "Usuario" label
    And we fill the "Contraseña" label
    And we tap the "LOGIN" button
    Then we has login and we are in the "Productos" screen