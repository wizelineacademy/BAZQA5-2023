Feature: Agregar producto

    @regression @smoke
    Scenario: Agregar producto al carrito
      Given Dado que el usuario ya esta logueado
      When Agregar un producto al carrito
      Then Se muestra producto en carrito con nombre y precio correctos
      And Validar nombre y precio del artículo