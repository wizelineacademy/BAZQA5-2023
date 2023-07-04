from screens.buy_products_screen import BuyProductsScreen
import time
from behave import *


@Given("Doy click en el carrito")
def step_impl(context):
    buyProducts = BuyProductsScreen(context)
    buyProducts.tap_element(*buyProducts.lbl_kart)


@When('Verifico que el carrito no tenga productos y en caso de tenerlo lo elimino')
def step_impl(context):
    buyProducts = BuyProductsScreen(context)
    if buyProducts.verify_element(*buyProducts.lbl_remove):
        buyProducts.tap_element(*buyProducts.lbl_remove)
    else:
        print("No es necesario eliminar productos porque no existen articulos")


@Then('Regreso a la pantalla de productos')
def step_impl(context):
    buyProducts = BuyProductsScreen(context)
    buyProducts.tap_element(*buyProducts.lbl_buy_more)


@Then('Agrego al carrito el producto')
def step_impl(context):
    buyProducts = BuyProductsScreen(context)
    buyProducts.scroll1(*buyProducts.lbl_add)
    buyProducts.tap_element(*buyProducts.lbl_add)
    time.sleep(10)

