from behave import Given, When, Then
from screens.login_screen import LoginScreen
from screens.product_screen import ProductosScreen
from screens.product_car_screen import ProductCar
from utils.dictionaries.user_pass import LOGIN_TEXTS
from utils.dictionaries.Product_car_sreentext import CAR_SCREEN


@Given('we are in the "Login1" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=LOGIN_TEXTS.get('txt_username'))
    login_screen.fill_text(*login_screen.txt_password, value=LOGIN_TEXTS.get('txt_password'))
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.btn_first_item)
    context.first_item_title = productosscreen.get_text_of_element(*productosscreen.lbl_title_item)
    context.first_item_price = productosscreen.get_text_of_element(*productosscreen.price_first_item)


@Then("we tap on the car icon")
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.icon_car)


@Then("we validate that the product title is correct")
def step_impl(context):
    productcar = ProductCar(context)
    productcar.assert_text(*productcar.lbl_title_first_item_cart, value=CAR_SCREEN.get('.text("Sauce Labs Backpack")'))


@Then("we validate that the product price is the correct")
def step_impl(context):
    productcar = ProductCar(context)
    productcar.assert_text(*productcar.price_first_item_cart, value=CAR_SCREEN.get('.text("$29.99")'))
