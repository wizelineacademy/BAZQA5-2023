from behave import *
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen


@Given('estamos en la pantalla de inicio')
def step_impl(context):
    pass

@When('ingresa usuario')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text="standard_user")


@When('ingresa contraseña')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_password, text="secret_sauce")


@When('damos clic al botón')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.tap_element(*login_in_screen.btn_login)


@Then('entramos a la app "SWAGLABS"')
def step_impl(context):
    product = ProductosScreen(context)
    product.assert_text(*product.lbl_productos, text="PRODUCTS")
