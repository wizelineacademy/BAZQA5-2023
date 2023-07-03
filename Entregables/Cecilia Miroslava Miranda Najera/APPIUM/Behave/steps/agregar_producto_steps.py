from behave import When, Then
from screens.Productos_screen import ProductosScreen


@When("Agregar un producto al carrito")
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_add)


@Then("Se muestra producto en carrito con nombre y precio correctos")
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_car)


@Then("Validar nombre y precio del artículo")
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.nombre_producto,
                                 text="Sauce Labs Bike Light")
    productos_screen.assert_text(*productos_screen.precio_producto,
                                 text="$9.99")
