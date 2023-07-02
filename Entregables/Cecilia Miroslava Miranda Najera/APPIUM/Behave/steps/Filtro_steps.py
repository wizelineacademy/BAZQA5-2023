from screens.Filtro_screen import FiltroScreen
from behave import When, Then


@When("Dar tap en el botón de filtro")
def step_impl(context):
    Filtro_screen = FiltroScreen(context)
    Filtro_screen.tap_element(*Filtro_screen.btn_filtro)


@When("Seleccionar menor a mayor")
def step_impl(context):
    Filtro_screen = FiltroScreen(context)
    Filtro_screen.tap_element(*Filtro_screen.opt_menor_mayor)


@Then("Hacer scroll para obtener producto de mayor precio")
def step_impl(context):
    Filtro_screen = FiltroScreen(context)
    Filtro_screen.scroll_down(*Filtro_screen.max_product)


@Then("Validar que la lista de productos se ordene de manera correcta")
def step_impl(context):
    Filtro_screen = FiltroScreen(context)
    Filtro_screen.assert_text(
        *Filtro_screen.max_price, text="$49.99")
