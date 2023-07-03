from behave import Given, When, Then
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen


@Given('we are in the LOGIN screen 2')
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username, text='standard_user')
    log_in_screen.fill_text(*log_in_screen.txt_password, text='secret_sauce')
    log_in_screen.tap_element(*log_in_screen.btn_login)


@When('we tap on Agregar a carrito button from the first item')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_first_item)


@When('we tap on the cart icon')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.icon_car)


@Then('we validate that the product title is correct')
def step_impl(context):     # noqa: F811
    prod_screen = ProductosScreen(context)
    prod_screen.assert_text(*prod_screen.product_title, text=context.PROD)


@Then("we validate that the product price is correct")
def step_impl(context):
    prod_screen = ProductosScreen(context)
    prod_screen.assert_text(*prod_screen.product_price, text=context.PRICE)
