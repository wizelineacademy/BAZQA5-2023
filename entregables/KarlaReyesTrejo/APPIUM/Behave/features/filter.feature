Feature: FILTER PRODUCT

      @regresion
      Scenario: FILTER PRODUCT
        Given we are in the product filter
        When we select from low to high
        When we validate lower price
        Then we validate ordering