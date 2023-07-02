from behave import *
from screens.productos_screen import ProductosScreen
from screens.product_cart_screen import CarritoScreen



@When('We click on add to the cart of the first product')
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.btn_first_item)
    context.first_item_title = productosscreen.get_text_of_element(
        *productosscreen.lbl_title_item
    )
    pass

@When('tap on the card icon')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.icon_cart)


@Then('We validate that the product, price and title information is correct')
def step_impl(context):
    productCartScreen = CarritoScreen(context)
    productCartScreen.assert_text(
        *productCartScreen.lbl_title_first_item_cart, text=context.first_item_title
    )

