from screens.login_screen import LoginScreen
from screens.product_car_screen import ProductCar
from screens.product_screen import ProductosScreen
from behave import *

@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=context.STANDARD_USER)
    login_screen.fill_text(*login_screen.txt_password, value=context.PASSWORD)
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.btn_first_item)
    context.first_item_title = productosscreen.get_text_of_element(*productosscreen.lbl_title_item)
    context.first_item_price = productosscreen.get_text_of_element(*productosscreen.price_first_item)
    pass


@Then("we tap on the car icon")
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.icon_car)
    pass


@Then("we validate that the product title is correct")
def step_impl(context):
    productcar = ProductCar(context)
    productcar.assert_text(*productcar.lbl_title_first_item_cart, value=context.first_item_title)
    pass


@Then("we validate that the product price is correct")
def step_impl(context):
    productcar = ProductCar(context)
    productcar.assert_text(*productcar.price_first_item_cart, value=context.first_item_price)
    pass