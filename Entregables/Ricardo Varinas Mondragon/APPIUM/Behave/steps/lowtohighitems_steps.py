from behave import *
from screens.product_screen import ProductosScreen


@Given('we are in the screen of products ordered by name')
def step_impl(context):

    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, text='PRODUCTOS')


@When('we tap on filter botton')
def step_impl(context):

    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_filter)


@When('we select the opcion "Price(low to high)"')
def step_impl(context):

    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_sortitem)


@Then('we validate the ordered by low to high price')
def step_impl(context):

    productos_screen = ProductosScreen(context)

    low_price = productos_screen.get_text_of_element(*productos_screen.lbl_price_low)
    high_price = productos_screen.get_text_of_element(*productos_screen.lbl_price_high)

    if low_price < high_price:
        return True
