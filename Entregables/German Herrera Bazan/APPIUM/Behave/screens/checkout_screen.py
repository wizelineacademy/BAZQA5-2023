from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CheckoutScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.add_product1 = (
            By.XPATH, '(//android.view.ViewGroup'
                      '[@content-desc="test-AÑADIR A CARRITO"])[1]'
        )
        self.add_product2 = (
            By.XPATH, '(//android.view.ViewGroup'
                      '[@content-desc="test-AÑADIR A CARRITO"])[2]'
                      '/android.widget.TextView'
        )
        self.tap_cart = (
            By.XPATH, '//android.view.ViewGroup'
                      '[@content-desc="test-Carrito"]'
                      '/android.view.ViewGroup/android.widget.ImageView'
        )
        self.button_checkout = (
            By.XPATH, '//android.view.ViewGroup'
                      '[@content-desc="test-CHECKOUT"]'
                      '/android.widget.TextView'
        )
        self.form_name = (
            By.XPATH, '//android.widget.EditText[@content-desc="test-Nombre"]'
        )
        self.form_last_name = (
            By.XPATH, '//android.widget.EditText'
                      '[@content-desc="test-Apellido"]'
        )
        self.form_postal_code = (
            By.XPATH, '//android.widget.EditText'
                      '[@content-desc="test-Código postal"]'
        )
        self.button_continue = (
            By.XPATH, '//android.view.ViewGroup'
                      '[@content-desc="test-CONTINUAR"]'
                      '/android.widget.TextView'
        )
        self.button_terminar = (
            By.ACCESSIBILITY_ID, "test-TERMINAR"
        )
        self.checkout_page = (
            By.XPATH, '//android.widget.ScrollView'
                      '[@content-desc="test-CHECKOUT: COMPLETADO!"]'
                      '/android.view.ViewGroup/android.widget.TextView[1]'
        )
