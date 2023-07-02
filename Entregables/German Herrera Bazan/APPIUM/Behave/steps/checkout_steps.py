import allure
from behave import Given, When, Then
from screens.checkout_screen import CheckoutScreen
from utils.dictionaries.checkout_texts import FORM, FINAL_PAGE_TEXTS


@Given('the user has added multiple items to the shopping cart')
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.tap_element(*checkout.add_product2)
    checkout.tap_element(*checkout.add_product1)


@When('the user selects the cart option')
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.tap_element(*checkout.tap_cart)


@When('the purchase confirmation screen is displayed')
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.scroll_down()
    checkout.tap_element(*checkout.button_checkout)


@When('customer data is entered')
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.fill_text(
        *checkout.form_name, text=FORM.get("NAME")
    )
    checkout.fill_text(
        *checkout.form_last_name, text=FORM.get("LAST_NAME")
    )
    checkout.fill_text(
        *checkout.form_postal_code, text=FORM.get("POSTAL_CODE")
    )


@When('I tap the continue button')
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.tap_element(*checkout.button_continue)


@When('we scroll to find the button')
def test_scroll(context):
    checkout = CheckoutScreen(context)
    checkout.scroll_down()


@When("we tap on the terminar button")
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.tap_element(*checkout.button_terminar)


@Then('you should be redirected to the order processed screen')
def step_impl(context):  # noqa: F811
    checkout = CheckoutScreen(context)
    checkout.assert_text(
        *checkout.checkout_page, text=FINAL_PAGE_TEXTS.get("FINAL_PAGE")
    )

    # Captura de imagen del último paso como evidencia.
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="Captura de pantalla",
                  attachment_type=allure.attachment_type.PNG)
