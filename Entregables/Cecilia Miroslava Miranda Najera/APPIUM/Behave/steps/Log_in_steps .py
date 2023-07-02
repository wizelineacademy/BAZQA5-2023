from behave import Given, When, Then, Step
from screens.Log_in_screen import LoginScreen
from screens.Productos_screen import ProductosScreen
from utils.dictionaries.Log_in_text import LOGIN_TEXTS


@Step("Dado que el usuario ya esta logueado")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username,
                            text=LOGIN_TEXTS.get('txt_username'))
    log_in_screen.fill_text(*log_in_screen.txt_password,
                            text=LOGIN_TEXTS.get('txt_password'))
    log_in_screen.tap_element(*log_in_screen.btn_login)


@Given("Ingreso usuario")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username,
                            text=LOGIN_TEXTS.get('txt_username'))


@Given("Ingreso contraseña")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_password,
                            text=LOGIN_TEXTS.get('txt_password'))


@When("Dar tap en botón de login")
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.tap_element(*log_in_screen.btn_login)


@Then("Se debe mostrar pantalla de productos")
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos,
                                 text="PRODUCTS")
