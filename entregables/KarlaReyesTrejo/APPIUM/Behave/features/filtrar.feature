Feature: Filtrar productos

      @regresion
      Scenario: FILTER PRODUCT
        Given estamos en el filtro de productos
        When seleccionamos de menor a mayor
        When validamos menor precio
        Then validamos ordenamiento