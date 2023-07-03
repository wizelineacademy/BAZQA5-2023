from behave import When, Given, Then
from screens.log_in_screen import LoginScreen
from screens.products_screen import ProductosScreen
from utils.dictionaries.input_data import LOGIN_TEXTS


@Given("Tengo la aplicacion de saucelabs")
def step_impl(context):
    LoginScreen(context)


@When("Ingreso 'usuario' correcto")
def step_impl(context):
    usuario = LOGIN_TEXTS.get("txt_username")
    loginscreen = LoginScreen(context)
    loginscreen.fill_text(*loginscreen.txt_username, text=usuario)


@When("Ingreso 'contrasena' correcta")
def step_impl(context):
    password = LOGIN_TEXTS.get("txt_password")
    loginscreen = LoginScreen(context)
    loginscreen.fill_text(*loginscreen.txt_password, text=password)


@When("Doy en opcion 'login'")
def step_impl(context):
    loginscreen = LoginScreen(context)
    loginscreen.tap_element(*loginscreen.btn_login)


@Then("Logro visualizar el titulo 'PRODUCTOS'")
def step_impl(context):
    text_productos = LOGIN_TEXTS.get("text_homepage")
    productscreen = ProductosScreen(context)
    productscreen.assert_text(*productscreen.lbl_productos,
                              text=text_productos)


@Given("Ingreso a la app con datos correctos")
def step_impl(context):
    usuario = LOGIN_TEXTS.get("txt_username")
    password = LOGIN_TEXTS.get("txt_password")
    loginscreen = LoginScreen(context)
    loginscreen.fill_text(*loginscreen.txt_username, text=usuario)
    loginscreen.fill_text(*loginscreen.txt_password, text=password)
    loginscreen.tap_element(*loginscreen.btn_login)
