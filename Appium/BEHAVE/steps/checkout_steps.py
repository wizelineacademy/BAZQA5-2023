from screens.checkout_screen import Checkout
from screens.login_screen import LoginScreen
from screens.product_car_screen import ProductCar
from screens.productos_screen import ProductosScreen
from screens.purchase_confirmation_screen import PuchaseConfirmacion
from screens.resumen_screen import Resumen
from utils.dictionaries.checkout_text import FORM, PAGE_TEXTS
from behave import *

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



@When('we scroll to find the button "TERMINAR"')
def test_scroll(context):
    resumen = Resumen(context)
    resumen.scroll1(*resumen.btn_terminar)



@When("we tap on the TERMINAR button")
def test_scroll(context):
    resumen = Resumen(context)
    resumen.tap_element(*resumen.btn_terminar)


@Then('the message "GRACIAS POR SU ORDEN" is displayed')
def test_scroll(context):
    puchaseconfirmacion = PuchaseConfirmacion(context)
    puchaseconfirmacion.assert_text(
        *puchaseconfirmacion.message_confirmation, value=PAGE_TEXTS.get("FINAL_PAGE")
    )
