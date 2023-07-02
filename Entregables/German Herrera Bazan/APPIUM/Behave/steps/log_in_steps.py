import allure
from behave import Given, When, Then
from screens.log_in_screen import LoginScreen
from utils.dictionaries.log_in_texts import LOGIN_TEXTS, PRODUCT_TEXTS


@Given('I am in the Sauce Labs application')
def step_impl(context):  # noqa: F811
    login_screen = LoginScreen(context)
    login_screen.find_element(*login_screen.login_screen)


@When('Enter my username')
def step_impl(context):  # noqa: F811
    login_screen = LoginScreen(context)
    login_screen.fill_text(
        *login_screen.txt_username, text=LOGIN_TEXTS.get("txt_username")
    )


@When('Enter my password')
def step_impl(context):  # noqa: F811
    login_screen = LoginScreen(context)
    login_screen.fill_text(
        *login_screen.txt_password, text=LOGIN_TEXTS.get("txt_password")
    )


@When('I tap the login')
def step_impl(context):  # noqa: F811
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('I can see title Products')
def step_impl(context):  # noqa: F811
    login_screen = LoginScreen(context)
    login_screen.assert_text(
        *login_screen.home_page, text=PRODUCT_TEXTS.get('PRODUCT_PAGE')
    )
    # Captura de imagen del último paso como evidencia.
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="Captura de pantalla",
                  attachment_type=allure.attachment_type.PNG)
