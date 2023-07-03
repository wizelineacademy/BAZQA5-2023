from screens.login_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.Product_detail_screen import Product_Detail
from utils.dictionaries.product_detail import DETAIL
from utils.dictionaries.log_in_text import LOGIN_TEXTS
from behave import *

@Given('we have been logged in app')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text=LOGIN_TEXTS.get('txt_username'))
    login_screen.fill_text(*login_screen.txt_password, text=LOGIN_TEXTS.get('txt_password'))
    login_screen.tap_element(*login_screen.btn_login)

@When('we tap on the first product to see the detail')
def step_impl(context):
    productosScreen = ProductosScreen(context)
    productosScreen.tap_element(*productosScreen.Producto_1_IMG)


@When('we validate the header is displayed')
def step_impl(context):
    ProductDetailScreen = Product_Detail(context)
    ProductDetailScreen.assert_text(*ProductDetailScreen.header_title, text="REGRESO A PRODUCTOS")


@Then('we validate that the product title and price on the description is correct')
def step_impl(context):
    productDetailScreen = Product_Detail(context)
    productDetailScreen.scroll1(*productDetailScreen.ProductPrice)
    productDetailScreen.scroll1(*productDetailScreen.ProductName)
    productDetailScreen.assert_text(*productDetailScreen.ProductPrice, text=DETAIL.get("PRODUCT_PRICE"))
    productDetailScreen.assert_text(*productDetailScreen.ProductName, text=DETAIL.get("PRODUCT_NAME"))