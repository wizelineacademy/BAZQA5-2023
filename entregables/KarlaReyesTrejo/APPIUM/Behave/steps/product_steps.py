from behave import *
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.log_in_text import *


@Given('estamos en la pantalla de productos')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text=LOGIN_TEXTS.get("txt_username"))
    login_in_screen.fill_text(*login_in_screen.txt_password, text=LOGIN_TEXTS.get("txt_password"))
    login_in_screen.tap_element(*login_in_screen.btn_login)


@When('seleccionamos un producto')
def step_impl(context):
    product = ProductosScreen(context)
    product.tap_element(*product.detail_product)

@Then('validar detalle del producto')
def step_impl(context):
    datos_product = ProductosScreen(context)
    datos_product.assert_text(*datos_product.lbl_price, text=SEE_PRODUCT.get("price"))
    datos_product.assert_text(*datos_product.lbl_product_name, text=SEE_PRODUCT.get("product_name"))
