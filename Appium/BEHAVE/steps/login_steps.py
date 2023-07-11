
from BEHAVE.screens.login_screen import LoginScreen
from BEHAVE.screens.product_screen import ProductosScreen
from behave import *


@Given('we are in the "LOGIN" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.assert_text(*login_screen.txt_username, value=context.BTN_LOGIN)


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=context.STANDARD_USER)


@Then('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password, value=context.PASSWORD)


@Then('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we has loggin correctly we are in the "Productos" screen')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, value=context.FIRST_ELEMENT)