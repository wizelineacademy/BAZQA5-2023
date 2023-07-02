from behave import *
from screens.product_screen import ProductosScreen
from screens.cart_screen import CartScreen
from screens.checkout_screen import CheckoutScreen
from screens.checkoutdetail_screen import CheckoutDetailScreen
from screens.thankyupage_screen import ThankyuScreen
from utils.dictionaries.log_in_text import PERSONAL_INFO
from utils.common_actions import CommonActions


@Given('we add two items in the cart')
def step_impl(context):

    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_addcarrito_firstitem)
    productos_screen.tap_element(*productos_screen.btn_addcarrito_seconditem)


@When('we tap on the icon cart')
def step_impl(context):

    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.icon_car)


@When('we tap on the option "CHECKOUT"')
def step_impl(context):
    swipe = CommonActions.scroll_screen(context)
    cart_screen = CartScreen(context)
    cart_screen.tap_element(*cart_screen.btn_checkout)


@When('we add the personal info')
def step_impl(context):

    checkout_screen = CheckoutScreen(context)
    checkout_screen.fill_text(*checkout_screen.input_name, text=PERSONAL_INFO.get("first_name"))
    checkout_screen.fill_text(*checkout_screen.input_lastname, text=PERSONAL_INFO.get("last_name"))
    checkout_screen.fill_text(*checkout_screen.input_zipcode, text=PERSONAL_INFO.get("zip_code"))


@When('we tap on "CONTINUAR"')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.tap_element(*checkout_screen.btn_continue)


@When('we tap on "TERMINAR"')
def step_impl(context):

    swipe = CommonActions.scroll_screen(context)
    checkout_detail = CheckoutDetailScreen(context)
    checkout_detail.tap_element(*checkout_detail.btn_finish)


@Then('we validate that the thankyu page message succesfull')
def step_impl(context):

    thankyu_screen = ThankyuScreen(context)
    thankyu_screen.assert_text(*thankyu_screen.lbl_thankyu, text="GRACIAS POR SU ORDEN")
