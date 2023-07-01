Feature: Filtrar productos

      @Regression
      Scenario: Filtrar productos de menor a mayor
            Given Dado que el usuario ya esta logueado
            When Dar tap en el botón de filtro
            And Seleccionar menor a mayor
            Then Validar que la lista de productos se ordene de manera correcta