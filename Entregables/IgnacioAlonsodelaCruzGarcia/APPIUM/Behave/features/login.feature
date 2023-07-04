Feature: Log In

    @regression @smoke
    Scenario: Prueba de usuario exitoso
      Given Tengo la aplicacion de saucelabs
      When Ingreso 'usuario' correcto
      And Ingreso 'contrasena' correcta
      And Doy en opcion 'login'
      Then Logro visualizar el titulo 'PRODUCTOS'
