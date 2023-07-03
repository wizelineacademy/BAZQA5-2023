from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.checkout_text import form, PAGE_TEXTS
from screens.summary_screen import Resumen
from screens.confirmacion_screens import Confirmation
from screens.checkout_screens import Checkout
from behave import Given, When, Then
from screens.cart_screens import CartScreen
from utils.dictionaries.checkout_text import PAGE_TEXTS

@Given('we are in the LOGIN screen 5')
def step_impl(context):
    log_in_screen = LoginScreen(context)
    log_in_screen.fill_text(*log_in_screen.txt_username, text='standard_user')
    log_in_screen.fill_text(*log_in_screen.txt_password, text='secret_sauce')
    log_in_screen.tap_element(*log_in_screen.btn_login)


@When('we add the products to the cart')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_first_item)


@When('we select the shopping cart')
def step_impl(context):     # noqa: F811
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.icon_car)


@When('we select checkout button')
def step_impl(context):     # noqa: F811
    cart_screens = CartScreen(context)
    cart_screens.tap_element(*cart_screens.btn_checkout)


@When('we enter customer information')
def step_impl(context):     # noqa: F811
    checkout = Checkout(context)
    checkout.fill_text(*checkout.txt_name, text=form.get("NAME"))
    checkout.fill_text(*checkout.txt_apellido, text=form.get("LAST_NAME"))
    checkout.fill_text(*checkout.txt_codigopostal,
                       text=form.get("POSTAL_CODE")
                       )


@When('we press continue button')
def step_impl(context):     # noqa: F811
    checkout = Checkout(context)
    checkout.tap_element(*checkout.btn_continuar)


@When('we scroll to find the finish button')
def step_impl(contex):      # noqa: F811
    resumen = Resumen(contex)
    resumen.scroll1(*resumen.btn_terminar)


@When('we press the finish button')
def step_impl(context):     # noqa: F811
    resumen = Resumen(context)
    resumen.tap_element(*resumen.btn_terminar)


@Then('we show purchase success screen')
def step_impl(context):     # noqa: F811
    confirm = Confirmation(context)
    confirm.assert_text(
        *confirm.message_confirmation, text=PAGE_TEXTS.get("FINAL_PAGE"))
