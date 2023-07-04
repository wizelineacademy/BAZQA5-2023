from behave import *
from screens.log_in_screen import LoginScreen
from screens.products_screen import ProductosScreen

@Given("Tengo la aplicaciòn")
def step_impl(context):
    pass

@When("Ingreso usuario")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username, text="standard_user")

@When("Ingreso password")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_password, text="secret_sauce")

@When("Doy click en Ingresar")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.tap_element(*log_in_screen.btn_login)

@Then("Logro visualizar el titulo de Productos")
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, value="PRODUCTOS")
