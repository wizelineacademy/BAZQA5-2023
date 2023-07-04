Feature: Agregar al carrito
  @regresion
  Scenario: ADD CART

    Given estamos dentro de la app
    When añadir primer producto
    When validar en el carrito
    Then validar nombre y precio del producto
