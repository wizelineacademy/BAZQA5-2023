Feature: Shopping Cart

    @regression
    Scenario: Agregar producto al carrito de compra
      Given Ingreso a la app con datos correctos
      When Elijo el 'producto'
      And Elijo 'Añadir a carrito'
      And Elijo el 'carrito de compra'
      Then Visualizo el carrito
      And Visualizo el 'nombre' del producto agregado al carrito
      And Visualizo el 'precio' del producto agregado al carrito