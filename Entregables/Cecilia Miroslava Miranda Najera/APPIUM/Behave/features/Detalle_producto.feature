Feature: Detalle del producto

    @regression @smoke
    Scenario: Agregar producto al carrito
      Given Dado que el usuario ya esta logueado
      When se encuentre en el detalle del producto
      Then Visualizar el detalle y validar nombre
      And Hacer scroll

