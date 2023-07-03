from screens.login_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS
from behave import *


@Given('we are in the LOGIN screen')
def step_impl(context):
    pass


@When('we fill the user label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text=LOGIN_TEXTS.get('txt_username'))


@When('we fill the password label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password, text=LOGIN_TEXTS.get('txt_password'))


@When('we tap the LOGIN button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we has loggin correctly we are in the Products screen')
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.assert_text(
        *productosscreen.lbl_productos, text="PRODUCTOS")
