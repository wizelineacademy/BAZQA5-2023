from Behave.screens.login_screen import Login
from Behave.screens.product_car_screen import Product
from Behave.screens.productos_screen import Prod
from behave import *




@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = Login(context)
    login_screen.fill_text(*login_screen.txt_username, value=context.STANDARD_USER)
    login_screen.fill_text(*login_screen.txt_password, value=context.PASSWORD)
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.btn_first_item)
    context.first_item_title = prod.get_text_of_element(
        *prod.lbl_title_item
    )
    context.first_item_price = prod.get_text_of_element(
        *prod.price_first_item
    )
    pass


@When("we tap on the car icon")
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.icon_car)
    pass


@Then("we validate that the product title is correct")
def step_impl(context):
    product = Product(context)
    product.assert_text(
        *product.lbl_title_first_item_cart, value=context.first_item_title
    )
    pass


@Then("we validate that the product price is correct")
def step_impl(context):
    product = Product(context)
    product.assert_text(
        *product.price_first_item_cart, value=context.first_item_price
    )
    pass