from behave import Given, When, Then
from screens.products_screen import ProductosScreen
from screens.shopping_cart_screen import ShoppingCartScreen
from screens.checkout_info_screen import CheckoutInfoScreen
from screens.checkout_resumen_screen import CheckoutResumenScreen
from screens.checkout_completado_screen import CheckoutCompletadoScreen
from utils.dictionaries.input_data import CART_TEXTS, CHECKOUT_TEXTS


@Given("Agrego los 'productos' al carrito y doy en 'carrito'")
def step_impl(context):
    product_screen = ProductosScreen(context)
    product_screen.tap_element(*product_screen.lbl_anadir_a_carrito)
    product_screen.tap_element(*product_screen.opc_carrito)


@When("Visualizo el carrito y doy en 'checkout'")
def step_impl(context):
    text_checkout = CART_TEXTS.get("txt_checkout")
    shopping_cart_screen = ShoppingCartScreen(context)
    shopping_cart_screen.scroll_into_element_tap(text_checkout)


@When("Ingreso informacion y doy en continuar")
def step_impl(context):
    text_nombre_usuario = CHECKOUT_TEXTS.get("txt_nombre_usuario")
    text_apellido_usuario = CHECKOUT_TEXTS.get("txt_ap_usuario")
    text_codigo_postal = CHECKOUT_TEXTS.get("txt_cp")
    checkout_info_screen = CheckoutInfoScreen(context)
    checkout_info_screen.fill_text(*checkout_info_screen.txt_nombre,
                                   text=text_nombre_usuario)
    checkout_info_screen.fill_text(*checkout_info_screen.txt_apellido,
                                   text=text_apellido_usuario)
    checkout_info_screen.fill_text(*checkout_info_screen.txt_codigo_postal,
                                   text=text_codigo_postal)
    checkout_info_screen.tap_element(*checkout_info_screen.btn_continuar)


@Then("Se muestra el resumen y doy en Terminar")
def step_impl(context):
    text_terminar = CHECKOUT_TEXTS.get("txt_terminar")
    checkout_resumen_screen = CheckoutResumenScreen(context)
    checkout_resumen_screen.scroll_into_element_tap(text_terminar)


@Then("Visualizo pagina 'terminado'")
def step_impl(context):
    txt_title = CHECKOUT_TEXTS.get("txt_title_checkout_terminado")
    checkout_completado_screen = CheckoutCompletadoScreen(context)
    checkout_completado_screen.assert_text(*checkout_completado_screen
                                           .lbl_title,
                                           text=txt_title)


@Then("Visualizo gracias")
def step_impl(context):
    txt_gracias = CHECKOUT_TEXTS.get("txt_gracias")
    checkout_completado_screen = CheckoutCompletadoScreen(context)
    checkout_completado_screen.assert_text(*checkout_completado_screen.
                                           lbl_gracias,
                                           text=txt_gracias)
