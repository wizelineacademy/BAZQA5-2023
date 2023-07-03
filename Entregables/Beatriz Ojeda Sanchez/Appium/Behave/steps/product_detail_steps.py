from Behave.screens.productos_screen import Prod
from Behave.screens.product_detail_screen import Details
from Behave.extras.dictionaries.product_detail_text import DETAIL
from behave import *

@When('we tap on the first product to see the detail')
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.Producto_1_IMG)
    pass


@Then("we validate the header is displayed")
def step_impl(context):
    details = Details(context)
    details.assert_text(*details.header_title, value="REGRESO A PRODUCTOS")
    pass


@Then("we validate that the product title on the description is correct")
def step_impl(context):
    details = Details(context)
    details.assert_text(*Details.ProductName, value=DETAIL.get("PRODUCT_NAME"))
    pass


@Then("we validate that the product price on the description is correct")
def step_impl(context):
    details = Details(context)
    details.scroll1(*details.ProductPrice)
    details.assert_text(*details.ProductPrice, value=DETAIL.get("PRODUCT_PRICE"))
    pass