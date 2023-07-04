from screens.filtro_screen import FiltroScreen
from behave import When, Then


@When("Dar tap en el botón de filtro")
def step_impl(context):
    filtro_screen = FiltroScreen(context)
    filtro_screen.tap_element(*filtro_screen.btn_filtro)


@When("Seleccionar menor a mayor")
def step_impl(context):
    filtro_screen = FiltroScreen(context)
    filtro_screen.tap_element(*filtro_screen.opt_menor_mayor)


@Then("Hacer scroll para obtener producto de mayor precio")
def step_impl(context):
    filtro_screen = FiltroScreen(context)
    filtro_screen.scroll_down(*filtro_screen.max_product)


@Then("Validar que la lista de productos se ordene de manera correcta")
def step_impl(context):
    filtro_screen = FiltroScreen(context)
    if filtro_screen.min_price < filtro_screen.max_price:
        return True
    else:
        return False




