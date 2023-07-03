from behave import When, Then
from screens.products_screen import ProductosScreen
from utils.dictionaries.input_data import ORDER_BY_PRICE_TEXTS


@When("Elijo 'filtro'")
def step_impl(context):
    product_screen = ProductosScreen(context)
    product_screen.tap_element(*product_screen.opc_filtro)


@When("Doy ordenar por precio 'de menor a mayor'")
def step_impl(context):
    product_screen = ProductosScreen(context)
    product_screen.tap_element(*product_screen.opc_minor_to_major)


@Then("Visualizo el primer producto con precio menor")
def step_impl(context):
    text_precio_menor = ORDER_BY_PRICE_TEXTS.get("txt_precio_menor")
    product_screen = ProductosScreen(context)
    product_screen.assert_text(*product_screen
                               .lbl_precio_bajo,
                               text=text_precio_menor)


@Then("Visualizo el ultimo producto con precio mayor")
def step_impl(context):
    text_precio_mayor = ORDER_BY_PRICE_TEXTS.get("txt_precio_mayor")
    product_screen = ProductosScreen(context)
    product_screen.assert_text(*product_screen
                               .scroll_down_precio_alto,
                               text=text_precio_mayor)
