from behave import When, Then
from screens.products_screen import ProductosScreen
from screens.product_detail_screen import ProductDetailScreen
from screens.shopping_cart_screen import ShoppingCartScreen
from utils.dictionaries.input_data import PRODUCT_TEXTS, CART_TEXTS


@When("Elijo 'producto'")
def step_impl(context):
    text_product_name = PRODUCT_TEXTS.get("txt_productname")
    products_screen = ProductosScreen(context)
    products_screen.scroll_into_element_tap(text_product_name)


@When("Elijo 'Añadir a carrito'")
def step_impl(context):
    text_anadir_carrito = PRODUCT_TEXTS.get("txt_add_cart")
    product_detail_screen = ProductDetailScreen(context)
    product_detail_screen.scroll_into_element(text_anadir_carrito)
    product_detail_screen.tap_element(*product_detail_screen
                                      .lbl_anadir_a_carrito)


@When("Elijo el 'carrito de compra'")
def step_impl(context):
    product_detail_screen = ProductDetailScreen(context)
    product_detail_screen.tap_element(*product_detail_screen.opc_carrito)


@Then("Visualizo el carrito")
def step_impl(context):
    text_titulo_tu_carrito = CART_TEXTS.get("txt_title_cart")
    shopping_cart_screen = ShoppingCartScreen(context)
    shopping_cart_screen.assert_text(*shopping_cart_screen
                                     .title_tu_carrito,
                                     text=text_titulo_tu_carrito)


@Then("Visualizo el 'nombre' del producto agregado al carrito")
def step_impl(context):
    text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
    shopping_cart_screen = ShoppingCartScreen(context)
    shopping_cart_screen.assert_text(*shopping_cart_screen
                                     .lbl_nombre_producto,
                                     text=text_nombre_producto)


@Then("Visualizo el 'precio' del producto agregado al carrito")
def step_impl(context):
    text_precio_producto = PRODUCT_TEXTS.get("txt_price")
    shopping_cart_screen = ShoppingCartScreen(context)
    shopping_cart_screen.assert_text(*shopping_cart_screen
                                     .lbl_precio_producto,
                                     text=text_precio_producto)
