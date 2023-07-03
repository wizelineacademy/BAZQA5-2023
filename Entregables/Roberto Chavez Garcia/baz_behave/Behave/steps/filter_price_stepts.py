from screens.login_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.price_filter import PRICE_FILTER
from behave import *


@When('we select filter icon')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.tap_element(*productosScreen.icon_filter)

@When('we select the option price low to high')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.tap_element(*productosScreen.option_lowest_to_highest)


@When('scroll on the screen')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.scroll1(*productosScreen.higher_product_name)

@Then('we validate the order products with the highest price')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.assert_text(
        *productosScreen.higher_product_price, text = PRICE_FILTER.get("HIGHER_PRICE")
    )
