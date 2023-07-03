Feature: Product_filter
  @Regresion
            Scenario: Filter_price_high_to_low
            Given we are in the LOGIN screen 4
            When we tap on "Filtro" button
            And we tap in "Price (high to low)" option
            Then we validate that the list of products is sorted by the filter from hightest to lowest
