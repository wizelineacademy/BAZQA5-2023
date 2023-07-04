Feature: Product Detail

    @regression @smoke
    Scenario: Visualizar el detalle de un producto
      Given Ingreso a la app con datos correctos
      When Elijo el 'producto'
      Then Visualizo el 'titulo' de 'detalle'
      And Visualizo el 'nombre' del 'producto' seleccionado
      And Visualizo el 'precio' del 'producto' seleccionado