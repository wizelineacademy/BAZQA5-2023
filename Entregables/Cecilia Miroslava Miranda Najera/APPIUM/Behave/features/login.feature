Feature: Log In

    @smoke
    Scenario: Login exitoso
      Given Ingreso usuario
      And Ingreso contraseña
      When Dar tap en botón de login
      Then Se debe mostrar pantalla de productos


