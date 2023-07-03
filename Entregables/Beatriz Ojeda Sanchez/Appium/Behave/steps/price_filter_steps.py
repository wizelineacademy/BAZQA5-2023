from Behave.screens.productos_screen import Prod
from Behave.extras.dictionaries.price_filter_text import PRICE_FILTER
from behave import *


@When("we select filter icon")
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.icon_filter)


@When("we select the option low to high")
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.option_lowest_to_highest)
    pass


@When("scroll on the screen")
def step_impl(context):
    prod = Prod(context)
    prod.scroll1(*prod.higher_product_name)
    pass

@Then("we validate the product with the highest price")
def step_impl(context):
    prod = Prod(context)
    prod.assert_text(
        *prod.higher_product_price, value=PRICE_FILTER.get("HIGHER_PRICE")
    )
    pass