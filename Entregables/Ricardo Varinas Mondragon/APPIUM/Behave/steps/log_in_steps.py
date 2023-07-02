from behave import *
from screens.log_in_screen import LoginScreen
from screens.product_screen import ProductosScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS


@Given('we are at the app Swag Labs')
def step_impl(context):
    pass


@When('we fill the user textbox')
def step_impl(context):

    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username, text=LOGIN_TEXTS.get('txt_username'))


@When('we fill the password textbox')
def step_impl(context):

    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_password, text=LOGIN_TEXTS.get('txt_password'))


@When('we click the login button')
def step_impl(context):

    log_in_screen = LoginScreen(context)
    log_in_screen.tap_element(*log_in_screen.btn_login)


@Then('we should be at the "PRODUCTOS" screen')
def step_impl(context):

    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, text='PRODUCTOS')
