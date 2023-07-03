from behave import Given, When, Then
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS


@Given('we are in the LOGIN screen')
def step_impl(context):     # noqa: F811
    pass


@When('we fill the Usuario label')
def step_impl(context):     # noqa: F811
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username,
                            text=LOGIN_TEXTS.get('txt_username')
                            )


@When('we fill the Contraseña label')
def step_impl(context):     # noqa: F811
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_password,
                            text=LOGIN_TEXTS.get('txt_password')
                            )


@When('we tap the LOGIN button')
def step_impl(context):     # noqa: F811
    log_in_screen = LoginScreen(context)
    log_in_screen.tap_element(*log_in_screen.btn_login)


@Then('we are in the Productos screen')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos,
                                 text=context.HOME)
