from screens.login_screen import LoginScreen
from screens.product_cart_screen import CarritoScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.checkout import form, PAGE_TEXTS
from screens.checkout_screen import Checkout
from screens.resumen_screen import Resumen
from screens.confirmation import Confirmation
from utils.dictionaries.confirmation import confirma
from behave import *

@When('we add the products to the cart')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.tap_element(*productosScreen.btn_first_item)


@When('we select the shopping cart')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.tap_element(*productosScreen.icon_cart)


@When('we select checkout button')
def step_impl(context):
    carritoScreen = CarritoScreen(context)
    carritoScreen.tap_element(*carritoScreen.btn_checkout)

@When('we enter customer information')
def step_impl(context):
    checkout = Checkout(context)
    checkout.fill_text(*checkout.txt_name, text=form.get("NAME"))
    checkout.fill_text(*checkout.txt_apellido, text=form.get("LAST_NAME"))
    checkout.fill_text(*checkout.txt_codigopostal, text=form.get("POSTAL_CODE"))


@When('we press continue button')
def step_impl(context):
    checkout = Checkout(context)
    checkout.tap_element(*checkout.btn_continuar)

@When('we scroll to find the finish button')
def step_impl(contex):
    resumen = Resumen(contex)
    resumen.scroll1(*resumen.btn_terminar)


@When('we press the finish button')
def step_impl(context):
    resumen = Resumen(context)
    resumen.tap_element(*resumen.btn_terminar)

@Then('we show purchase success screen')
def step_impl(context):
    confirm = Confirmation(context)
    confirm.assert_text(
        *confirm.message_confirmation, text=PAGE_TEXTS.get("FINAL_PAGE")
    )