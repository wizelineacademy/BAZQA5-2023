from behave import Given, When, Then
from screens.login_screen import LoginScreen
from screens.product_screen import ProductScreen
from screens.cart_screen import CartScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS, SEE_PRODUCT


@Given('we are inside the app')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text=LOGIN_TEXTS.get("txt_username"))
    login_in_screen.fill_text(*login_in_screen.txt_password, text=LOGIN_TEXTS.get("txt_password"))
    login_in_screen.tap_element(*login_in_screen.btn_login)


@When('add first product')
def step_impl(context):
    product = CartScreen(context)
    product.tap_element(*product.btn_Add_Cart)


@When('validate in the cart')
def step_impl(context):
    product = ProductScreen(context)
    product.tap_element(*product.icon_cart)


@Then('validate product name and price')
def step_impl(context):
    cart_screen = CartScreen(context)
    cart_screen.tap_element(*cart_screen.icon_cart)
    cart_screen.assert_text(*cart_screen.lbl_price_cart, text=SEE_PRODUCT.get("price"))
    cart_screen.assert_text(*cart_screen.lbl_product_name_cart, text=SEE_PRODUCT.get("product_name"))
