from behave import *
from screens.login_screen import LoginScreen
from screens.product_screen import ProductosScreen
from utils.dictionaries.user_pass import LOGIN_TEXTS


@Given('we are in the "LOGIN" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.assert_text(*login_screen.txt_username, value=LOGIN_TEXTS.get('txt_username'))


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=LOGIN_TEXTS.get('txt_username'))


@Then('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password, value=LOGIN_TEXTS.get('txt_password'))


@Then('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we has login and we are in the "Productos" screen')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, value=context.FIRST_ELEMENT)