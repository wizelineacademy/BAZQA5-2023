Feature: Filtrar productos

    @regression @smoke
    Scenario: Filtrar productos de menor a mayor
      Given Dado que el usuario ya esta logueado
      When Dar tap en el botón de filtro
      And Seleccionar menor a mayor
      Then Hacer scroll para obtener producto de mayor precio
      And Validar que la lista de productos se ordene de manera correcta
