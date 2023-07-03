from Behave.screens.checkout_screen import Check
from Behave.screens.login_screen import Login
from Behave.screens.product_car_screen import Product
from Behave.screens.productos_screen import Prod
from Behave.screens.purchase_confirmation_screen import Success
from Behave.screens.resumen_screen import Summary
from Behave.extras.dictionaries.checkout_text import FORM, PAGE_TEXTS
from behave import *

@When("we has added the first items to the shopping cart")
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.btn_first_item)
    pass

@When("we tap on the cart option")
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*prod.icon_car)
    pass


@When("we tap on CHECKOUT")
def step_impl(context):
    prod = Prod(context)
    prod.tap_element(*Prod.btn_checkout)
    pass


@When("We enter customer information")
def step_impl(context):
    check = Check(context)
    check.fill_text(*check.txt_name, value=FORM.get("NAME"))
    check.fill_text(*check.txt_apellido, value=FORM.get("LAST_NAME"))
    check.fill_text(*check.txt_codigopostal, value=FORM.get("POSTAL_CODE"))
    pass


@When("we tap the CONTINUAR button")
def step_impl(context):
    check = Check(context)
    check.tap_element(*check.btn_continuar)
    pass


@When('we scroll to find the button "TERMINAR"')
def test_scroll(context):
    summary = Summary(context)
    summary.scroll1(*summary.btn_terminar)
    pass


@When("we tap on the TERMINAR button")
def test_scroll(context):
    summary = Summary(context)
    summary.tap_element(*summary.btn_terminar)
    pass

@Then('the message "GRACIAS POR SU ORDEN" is displayed')
def test_scroll(context):
    success = Success(context)
    success.assert_text(
        *success.message_confirmation, value=PAGE_TEXTS.get("FINAL_PAGE")
    )
    pass