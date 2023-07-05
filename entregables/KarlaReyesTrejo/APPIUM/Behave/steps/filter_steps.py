from behave import *
from screens.log_in_screen import LoginScreen
from screens.filter_screen import FilterScreen
from utils.dictionaries.log_in_text import *


@Given('estamos en el filtro de productos')
def step_impl(context):
    login_in_screen = LoginScreen(context)
    login_in_screen.fill_text(*login_in_screen.txt_username, text=LOGIN_TEXTS.get("txt_username"))
    login_in_screen.fill_text(*login_in_screen.txt_password, text=LOGIN_TEXTS.get("txt_password"))
    login_in_screen.tap_element(*login_in_screen.btn_login)
    filter_price = FilterScreen(context)
    filter_price.tap_element(*filter_price.btn_filter)


@When('seleccionamos de menor a mayor')
def step_impl(context):
    filter_price = FilterScreen(context)
    filter_price.tap_element(*filter_price.btn_low_price)


@When('validamos menor precio')
def step_impl(context):
    filter_price = FilterScreen(context)
    filter_price.assert_text(*filter_price.lbl_low_price_item, text=PRICE_PRODUCT_FILTER.get("LOW_PRICE"))


@Then('validamos ordenamiento')
def step_impl(context):
    filter_price = FilterScreen(context)
    filter_price.tap_element(*filter_price.btn_filter)
    filter_price.tap_element(*filter_price.btn_high_price)
    filter_price.assert_text(*filter_price.lbl_high_price_item, text=PRICE_PRODUCT_FILTER.get("HIGH_PRICE"))
