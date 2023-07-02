from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CheckoutScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.input_name = (By.ACCESSIBILITY_ID, "test-Nombre")
        self.input_lastname = (By.ACCESSIBILITY_ID, "test-Apellido")
        self.input_zipcode = (By.ACCESSIBILITY_ID, "test-Código postal")
        self.btn_continue = (By.ACCESSIBILITY_ID, "test-CONTINUAR")
