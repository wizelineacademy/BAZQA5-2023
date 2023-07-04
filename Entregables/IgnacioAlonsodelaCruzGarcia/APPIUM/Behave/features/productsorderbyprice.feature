Feature: Products Order By Price

    @regression
    Scenario: Ordenar productos por precio de menor a mayor
      Given Ingreso a la app con datos correctos
      When Elijo 'filtro'
      And Doy ordenar por precio 'de menor a mayor'
      Then Visualizo el primer producto con precio menor
      And Visualizo el ultimo producto con precio mayor