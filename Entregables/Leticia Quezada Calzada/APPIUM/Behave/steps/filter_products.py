from behave import *
from screens.filter_products import FilterProductsScreen
from utils.dictionaries.filter_products import filterProducts


@Given('Ingreso a la opcion de filtro')
def step_impl(context):
    filterProducts = FilterProductsScreen(context)
    filterProducts.tap_element(*filterProducts.lbl_filtro)

@When('Seleccionar opcion de menor a mayor')
def step_impl(context):
    filterProducts = FilterProductsScreen(context)
    filterProducts.tap_element(*filterProducts.lbl_order)

@Then('Obtener la vista del producto de mayor precio')
def step_impl(context):
    filter_products = FilterProductsScreen(context)
    filter_products.scroll1(*filter_products.lbl_high_product)

@Then('Validar que la lista de productos se ordene de menor a mayor')
def step_impl(context):
    filter_products = FilterProductsScreen(context)
    filter_products.assert_text(*filter_products.lbl_high_product, value=filterProducts.get("Price_higher"))
    pass