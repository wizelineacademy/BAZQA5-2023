import allure
from behave import Given, When, Then
from screens.price_filter_screen import PriceFilter


@Given('you tapped on the sort filter')
def step_impl(context):  # noqa: F811
    price_filter = PriceFilter(context)
    price_filter.tap_element(*price_filter.tap_filter)


@When('I select the option Price from lowest to highest')
def step_impl(context):  # noqa: F811
    price_filter = PriceFilter(context)
    price_filter.tap_element(
        *price_filter.tap_low_to_high
    )
    context.lower_price = price_filter.get_text_of_element(
        *price_filter.lbl_lower_price
    )


@When('we validate the product with the least')
def step_impl(context):  # noqa: F811
    price_filter = PriceFilter(context)
    price_filter.assert_text(
        *price_filter.lbl_lower_price, text=context.lower_price
    )


@When('scroll on the screen')
def step_impl(context):  # noqa: F811
    price_filter = PriceFilter(context)
    price_filter.scroll_down()
    context.high_price = price_filter.get_text_of_element(
        *price_filter.lbl_high_price
    )


@Then('we validate the product with the highest price')
def step_impl(context):  # noqa: F811
    price_filter = PriceFilter(context)
    price_filter.assert_text(
        *price_filter.lbl_high_price, text=context.high_price
    )

    # Captura de imagen del último paso como evidencia.
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="Captura de pantalla",
                  attachment_type=allure.attachment_type.PNG)
