
from screens.product_screen import ProductosScreen
from behave import *


@When("we select filter icon")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.tap_element(*productscreen.icon_filter)


@When("we select the option low to high")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.tap_element(*productscreen.option_lowest_to_highest)



@When("scroll on the screen")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.scroll1(*productscreen.higher_product_name)


@Then("we validate the product with the highest price")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.assert_text(*productscreen.higher_product_price, value= context.PROD_LOW_NAME)
