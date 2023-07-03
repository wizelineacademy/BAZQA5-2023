from Behave.screens.login_screen import Login
from Behave.screens.productos_screen import Prod
from Behave.extras.dictionaries.login_text import HOME_TEXTS
from behave import *

@Given('we are in the "LOGIN" screen')
def step_impl(context):
    pass


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = Login(context)
    login_screen.fill_text(*login_screen.txt_username, value=context.STANDARD_USER)
    pass


@When('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = Login(context)
    login_screen.fill_text(*login_screen.txt_password, value=context.PASSWORD)
    pass


@When('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = Login(context)
    login_screen.tap_element(*login_screen.btn_login)
    pass


@Then('we has loggin correctly we are in the "Productos" screen')
def step_impl(context):
    prod = Prod(context)
    prod.assert_text(*prod.lbl_productos, value=HOME_TEXTS.get("HOME_PAGE"))
    pass