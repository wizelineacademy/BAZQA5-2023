from behave import *
from screens.products_screen import ProductosScreen
from utils.dictionaries.products_text import screen_products


@Given("Veo los productos")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.assert_text(*productscreen.lbl_productos, value=screen_products.get("title"))

@When("Selecciono producto y Comparo Nombre / Precio")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.scroll1(*productscreen.lbl_name_product)
    productscreen.tap_element(*productscreen.lbl_name_product)
    productscreen.assert_text(*productscreen.lbl_name_product, value=screen_products.get("name"))
    productscreen.assert_text(*productscreen.lbl_price_product, value=screen_products.get("price"))
    pass
