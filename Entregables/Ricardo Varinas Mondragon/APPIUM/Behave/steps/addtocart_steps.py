from behave import *
from screens.product_screen import ProductosScreen
from screens.item_screen import ItemScreen
from utils.common_actions import CommonActions
from screens.cart_screen import CartScreen


@Given('we are in the screen of the first item')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.img_prod_item)


@When('we tap on "AÑADIR A CARRITO"')
def step_impl(context):

    item_screen = ItemScreen(context)
    swipe = CommonActions.scroll_screen(context)

    context.item_singletitle = item_screen.get_text_of_element(*item_screen.lbl_item_single_title)
    context.item_singledescription = item_screen.get_text_of_element(*item_screen.lbl_item_description)
    context.item_singleprice = item_screen.get_text_of_element(*item_screen.lbl_item_single_price)

    item_screen.tap_element(*item_screen.btn_addcarrito_item)


@When('we tap on the card icon')
def step_impl(context):

    item_screen = ItemScreen(context)
    item_screen.tap_element(*item_screen.btn_cart)


@Then('we validate that the product title, price and description is correct')
def step_impl(context):

    cart_screen = CartScreen(context)
    description_item = ItemScreen(context)

    cart_screen.assert_text(*cart_screen.cart_title_item, text=context.item_singletitle)
    cart_screen.assert_text(*cart_screen.cart_description_item, text=context.item_singledescription)
    cart_screen.assert_text(*cart_screen.cart_price_item, text=context.item_singleprice)
