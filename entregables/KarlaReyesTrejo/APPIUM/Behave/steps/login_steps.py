from behave import Given, When, Then
from screens.login_screen import LoginScreen
from screens.product_screen import ProductScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS


@Given('we are on the home screen')
def step_impl(context):
    pass


@When('enter user')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text=LOGIN_TEXTS.get("txt_username"))


@When('enter password')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_password, text=LOGIN_TEXTS.get("txt_password"))


@When('we click the button')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.tap_element(*login_in_screen.btn_login)


@Then('we enter the app "SWAGLABS"')
def step_impl(context):
    product = ProductScreen(context)
    product.assert_text(*product.lbl_productos, text="PRODUCTS")
