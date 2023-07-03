import allure
from behave import Given, When, Then
from screens.add_product_screen import AddProduct


@Given("the user has added a product to the cart")
def step_impl(context):  # noqa: F811
    add_product = AddProduct(context)
    add_product.tap_element(*add_product.add_producto)


@When('the user selects the "view cart" option')
def step_impl(context):  # noqa: F811
    add_product = AddProduct(context)
    add_product.tap_element(*add_product.tap_cart)
    context.item_title = add_product.get_text_of_element(
        *add_product.lbl_title_item
    )
    context.price_product = add_product.get_text_of_element(
        *add_product.lbl_price_product
    )
    context.description_product = add_product.get_text_of_element(
        *add_product.lbl_description_product
    )


@Then("the user should see the product in the cart")
def step_impl(context):  # noqa: F811
    add_product = AddProduct(context)
    add_product.assert_text(
        *add_product.lbl_price_product, text=context.price_product
    )
    add_product.assert_text(
        *add_product.lbl_title_item, text=context.item_title
    )
    add_product.assert_text(
        *add_product.lbl_description_product, text=context.description_product
    )

    # Captura de imagen del último paso como evidencia.
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="Captura de pantalla",
                  attachment_type=allure.attachment_type.PNG)
