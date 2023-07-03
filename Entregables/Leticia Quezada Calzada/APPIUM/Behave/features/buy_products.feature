 Feature: Buy Products

  Background:
      Given Tengo la aplicaciòn
      When Ingreso usuario
      And Ingreso password
      And Doy click en Ingresar

    @regression @products
     Scenario: Eliminar registros del carrito
      Given Doy click en el carrito
      When Verifico que el carrito no tenga productos y en caso de tenerlo lo elimino
      Then Regreso a la pantalla de productos

   @regression @kart
    Scenario: Agregar producto al carrito
      Given Doy click en el carrito
      When Verifico que el carrito no tenga productos y en caso de tenerlo lo elimino
      Then Regreso a la pantalla de productos
      When Selecciono producto y Comparo Nombre / Precio
      Then Agrego al carrito el producto





