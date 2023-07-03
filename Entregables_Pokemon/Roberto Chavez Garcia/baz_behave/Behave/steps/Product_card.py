from behave import Given, When, Then
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.cart_screens import CartScreen
from utils.dictionaries.porduct_detailtext import DETAIL


@Given('we are in the LOGIN screen 3')
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username, text='standard_user')
    log_in_screen.fill_text(*log_in_screen.txt_password, text='secret_sauce')
    log_in_screen.tap_element(*log_in_screen.btn_login)


@When('we tap on the first product to see the detail')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_first_item)


@When('we tap on the card icon')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.icon_cart)


@Then('we validate that the product title on the description is correct')
def step_impl(context):     # noqa: F811
    cart_screens = CartScreen(context)
    cart_screens.assert_text(
      *cart_screens.ProductName, text=DETAIL.get("PRODUCT_NAME"))


@Then('we validate that the product price on the description is correct')
def step_impl(context):     # noqa: F811
    cart_screens = CartScreen(context)
    cart_screens.scroll1(*cart_screens.ProductPrice)
    cart_screens.assert_text(*cart_screens.ProductPrice,
                             text=DETAIL.get("PRODUCT_PRICE")
                             )
