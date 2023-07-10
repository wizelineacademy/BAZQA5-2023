from behave import Given, When, Then
from screens.login_screen import LoginScreen
from screens.product_screen import ProductScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS
from utils.dictionaries.log_in_text import SEE_PRODUCT


@Given('we are on the product screen')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text=LOGIN_TEXTS.get("txt_username"))
    login_in_screen.fill_text(*login_in_screen.txt_password, text=LOGIN_TEXTS.get("txt_password"))
    login_in_screen.tap_element(*login_in_screen.btn_login)


@When('we select a product')
def step_impl(context):
    product = ProductScreen(context)
    product.tap_element(*product.detail_product)


@Then('validate product detail')
def step_impl(context):
    datos_product = ProductScreen(context)
    datos_product.assert_text(*datos_product.lbl_price, text=SEE_PRODUCT.get("price"))
    datos_product.assert_text(*datos_product.lbl_product_name, text=SEE_PRODUCT.get("product_name"))
