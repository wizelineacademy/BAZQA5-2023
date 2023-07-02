from behave import When, Then
from screens.Detalle_producto_screen import DetalleProductoScreen


@When("se encuentre en el detalle del producto")
def step_impl(context):
    detalle_producto_screen = DetalleProductoScreen(context)
    detalle_producto_screen.tap_element(*detalle_producto_screen.select_producto)


@Then("Visualizar el detalle y validar nombre")
def step_impl(context):
    detalle_producto_screen = DetalleProductoScreen(context)
    detalle_producto_screen.assert_text(*detalle_producto_screen.desc_producto, text="Sauce Labs Backpack")


@Then("Hacer scroll")
def step_impl(context):
    detalle_producto_screen = DetalleProductoScreen(context)
    detalle_producto_screen.scroll_down(*detalle_producto_screen.price_producto)
    detalle_producto_screen.assert_text(*detalle_producto_screen.price_producto,
                                         text="$29.99")
