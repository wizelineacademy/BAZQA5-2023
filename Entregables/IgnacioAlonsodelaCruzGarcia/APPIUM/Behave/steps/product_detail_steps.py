from behave import When, Then
from screens.products_screen import ProductosScreen
from screens.product_detail_screen import ProductDetailScreen
from utils.dictionaries.input_data import PRODUCT_TEXTS


@When("Elijo el 'producto'")
def step_impl(context):
    text_product_name = PRODUCT_TEXTS.get("txt_productname")
    products_screen = ProductosScreen(context)
    products_screen.scroll_into_element_tap(text_product_name)


@Then("Visualizo el 'titulo' de 'detalle'")
def step_impl(context):
    text_title_product_detail = PRODUCT_TEXTS.get("txt_title_product_detail")
    product_detail_screen = ProductDetailScreen(context)
    product_detail_screen.assert_text(
        *product_detail_screen.lbl_title_product_detail,
        text=text_title_product_detail)


@Then("Visualizo el 'nombre' del 'producto' seleccionado")
def step_impl(context):
    text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
    product_detail_screen = ProductDetailScreen(context)
    product_detail_screen.assert_text(
        *product_detail_screen.scroll_down_product_name,
        text=text_nombre_producto)


@Then("Visualizo el 'precio' del 'producto' seleccionado")
def step_impl(context):
    text_precio_producto = PRODUCT_TEXTS.get("txt_price")
    product_detail_screen = ProductDetailScreen(context)
    product_detail_screen.assert_text(
        *product_detail_screen.scroll_down_product_price,
        text=text_precio_producto)
