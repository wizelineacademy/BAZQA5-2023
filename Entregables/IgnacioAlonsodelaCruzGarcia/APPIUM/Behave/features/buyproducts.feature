Feature: Comprar productos

    @regression @smoke
    Scenario: Ordenar productos por precio de menor a mayor
      Given Ingreso a la app con datos correctos
      And Agrego los 'productos' al carrito y doy en 'carrito'
      When Visualizo el carrito y doy en 'checkout'
      And Ingreso informacion y doy en continuar
      Then Se muestra el resumen y doy en Terminar
      And Visualizo pagina 'terminado'
      And Visualizo gracias