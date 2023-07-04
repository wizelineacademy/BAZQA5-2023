   Feature: See screen of products

  Background:
      Given Tengo la aplicaciòn
      When Ingreso usuario
      And Ingreso password
      And Doy click en Ingresar

    @regression @products
    Scenario: Validaciòn de pantalla de detalle en Productos
      Given Veo los productos
      When Selecciono producto y Comparo Nombre / Precio

