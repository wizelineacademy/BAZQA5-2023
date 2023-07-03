from behave import Given, Then
import allure
from screens.product__detail_screen import ProductosScreen
from screens.log_in_screen import LoginScreen
from utils.dictionaries.log_in_texts import LOGIN_TEXTS
from utils.dictionaries.product_detail_texts import PRODUCT_DETAIL


@step('login')  # noqa: F821
def step_impl(context):  # noqa: F811
    login_screen = LoginScreen(context)
    login_screen.fill_text(
        *login_screen.txt_username, text=LOGIN_TEXTS.get("txt_username")
    )
    login_screen.fill_text(
        *login_screen.txt_password, text=LOGIN_TEXTS.get("txt_password")
    )
    login_screen.tap_element(
        *login_screen.btn_login
    )


@Given('the user makes tap in the button of a product')
@allure.title("lo que sea")
def step_impl(context):  # noqa: F811
    allure.dynamic.title("Verificación de inicio de sesión exitoso")
    allure.dynamic.description("Verificación de inicio de sesión exitoso")
    allure.dynamic.feature("Inicio de sesión")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    product_screen = ProductosScreen(context)
    product_screen.tap_element(
        *product_screen.tap_product
    )


@Then('must be shown the product detail')
def step_impl(context):  # noqa: F811
    product_screen = ProductosScreen(context)
    product_screen.assert_text(
        *product_screen.product_name, text=PRODUCT_DETAIL.get("NAME_PRODUCT")
    )
    product_screen.assert_text(
        *product_screen.product_price, text=PRODUCT_DETAIL.get("PRICE_PRODUCT")
    )

    # Captura de imagen del último paso como evidencia.
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="Captura de pantalla",
                  attachment_type=allure.attachment_type.PNG)
