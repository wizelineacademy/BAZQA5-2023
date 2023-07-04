Feature: Filter of products

Background:
      Given Tengo la aplicaciòn
      When Ingreso usuario
      And Ingreso password
      And Doy click en Ingresar

    @regression @filter
    Scenario: Filtrar productos de menor a mayor precio
      Given Ingreso a la opcion de filtro
      When Seleccionar opcion de menor a mayor
      Then Obtener la vista del producto de mayor precio
      And Validar que la lista de productos se ordene de menor a mayor