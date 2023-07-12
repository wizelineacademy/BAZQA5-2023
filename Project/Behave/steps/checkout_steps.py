from screens.login_screen import LoginScreen
from screens.product_car_screen import ProductCar
from screens.product_screen import ProductosScreen
from screens.purchase_screen import PurchaseConfirmation
from utils.dictionaries.checkout_text import FORM
from screens.resumen_screen import Resumen
from screens.checkout_screen import Checkout
from behave import *
from utils.dictionaries.checkout_text import PAGE_TEXTS


@Given('we are in the "Login2" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=context.STANDARD_USER)
    login_screen.fill_text(*login_screen.txt_password, value=context.PASSWORD)
    login_screen.tap_element(*login_screen.btn_login)


@When("we has added the first items to the shopping cart")
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.btn_first_item)


@When("we tap on the cart option")
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.icon_car)


@When("we tap on CHECKOUT")
def step_impl(context):
    productcar = ProductCar(context)
    productcar.tap_element(*productcar.btn_checkout)


@When("We enter customer information")
def step_impl(context):
    checkout = Checkout(context)
    checkout.fill_text(*checkout.txt_name, value=FORM.get("NAME"))
    checkout.fill_text(*checkout.txt_apellido, value=FORM.get("LAST_NAME"))
    checkout.fill_text(*checkout.txt_codigopostal, value=FORM.get("POSTAL_CODE"))


@When("we tap the CONTINUAR button")
def step_impl(context):
    checkout = Checkout(context)
    checkout.tap_element(*checkout.btn_continuar)





@When("we tap on the TERMINAR button")
def step_impl(context):
    resumen = Resumen(context)
    resumen.tap_element(*resumen.btn_terminar)


@Then('the message "GRACIAS POR SU ORDEN" is displayed')
def step_impl(context):
    puchaseconfirmation = PurchaseConfirmation(context)
    puchaseconfirmation.assert_text(
        *puchaseconfirmation.message_confirmation, value=PAGE_TEXTS.get("FINAL_PAGE")
    )
