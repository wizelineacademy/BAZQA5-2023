from behave import *
from screens.product_screen import ProductosScreen
from screens.item_screen import ItemScreen
from utils.common_actions import CommonActions


@Given('we are in te "PRODUCTOS" screen')
def step_impl(context):

    producto_screen = ProductosScreen(context)
    context.item_title = producto_screen.get_text_of_element(*producto_screen.lbl_title_item)
    context.price_screen = producto_screen.get_text_of_element(*producto_screen.lbl_price_item)


@When('we tap on the first item')
def step_impl(context):

    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.img_prod_item)


@Then('we validate the name and price of the product')
def step_impl(context):

    item_screen = ItemScreen(context)

    swipe = CommonActions.scroll_screen(context)
    price_screen = ProductosScreen(context)

    item_screen.assert_text(*item_screen.lbl_item_single_title, text=context.item_title)
    item_screen.assert_text(*item_screen.lbl_item_single_price, text=context.price_screen)
