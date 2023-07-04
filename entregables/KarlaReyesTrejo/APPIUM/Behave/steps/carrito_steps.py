from behave import *

from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.carrito_screen import CarritoScreen
from utils.dictionaries.log_in_text import *


@Given('estamos dentro de la app')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text=LOGIN_TEXTS.get("txt_username"))
    login_in_screen.fill_text(*login_in_screen.txt_password, text=LOGIN_TEXTS.get("txt_password"))
    login_in_screen.tap_element(*login_in_screen.btn_login)

@When('añadir primer producto')
def step_impl(context):
    product = CarritoScreen(context)
    product.tap_element(*product.btn_Add_Cart)


@When('validar en el carrito')
def step_impl(context):
    product = ProductosScreen(context)
    product.tap_element(*product.icon_cart)




@Then('validar nombre y precio del producto')
def step_impl(context):
    carrito_screen = CarritoScreen(context)
    carrito_screen.tap_element(*carrito_screen.icon_cart)
    carrito_screen.assert_text(*carrito_screen.lbl_price_cart, text=SEE_PRODUCT.get("price"))
    carrito_screen.assert_text(*carrito_screen.lbl_product_name_cart, text=SEE_PRODUCT.get("product_name"))
