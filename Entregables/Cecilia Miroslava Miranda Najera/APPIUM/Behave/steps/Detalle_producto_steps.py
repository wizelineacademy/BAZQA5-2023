from behave import When, Then
from screens.Detalle_producto_screen import DetalleProductoScreen


@When("se encuentre en el detalle del producto")
def step_impl(context):
    Detalle_producto_screen = DetalleProductoScreen(context)
    Detalle_producto_screen.tap_element(*Detalle_producto_screen.select_producto)


@Then("Visualizar el detalle y validar nombre")
def step_impl(context):
    Detalle_productos_screen = DetalleProductoScreen(context)
    Detalle_productos_screen.assert_text(*Detalle_productos_screen.desc_producto, text="Sauce Labs Backpack")


@Then("Hacer scroll")
def step_impl(context):
    Detalle_productos_screen = DetalleProductoScreen(context)
    Detalle_productos_screen.scroll_down(*Detalle_productos_screen.price_producto)
    Detalle_productos_screen.assert_text(*Detalle_productos_screen.price_producto,
                                         text="$29.99")
