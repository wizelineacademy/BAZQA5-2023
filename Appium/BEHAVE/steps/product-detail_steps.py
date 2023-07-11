from BEHAVE.screens.login_screen import LoginScreen
from BEHAVE.screens.product_screen import ProductosScreen
from BEHAVE.screens.product_detail_screen import ProductDetail
from behave import *


@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=context.STANDARD_USER)
    login_screen.fill_text(*login_screen.txt_password, value=context.PASSWORD)
    login_screen.tap_element(*login_screen.btn_login)

@When('we tap on the first product to see the detail')
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.Producto_1_IMG)
    pass



@Then("we validate that the product title on the description is correct")
def step_impl(context):
    productdetail = ProductDetail(context)
    productdetail.assert_text(*productdetail.ProductName, text= context.PROD_HIGH_NAME)



@Then("we validate that the product price on the description is correct")
def step_impl(context):
    productdetail = ProductDetail(context)
    productdetail.scroll1(*productdetail.ProductPrice)
    productdetail.assert_text(*productdetail.ProductPrice, value= context.PRODUCT_PRICE)
