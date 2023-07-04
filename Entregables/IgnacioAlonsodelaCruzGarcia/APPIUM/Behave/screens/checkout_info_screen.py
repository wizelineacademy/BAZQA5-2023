from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class CheckoutInfoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_nombre = (By.ACCESSIBILITY_ID, "test-Nombre")
        self.txt_apellido = (By.ACCESSIBILITY_ID, "test-Apellido")
        self.txt_codigo_postal = (By.ACCESSIBILITY_ID, "test-Código postal")
        self.btn_continuar = (By.XPATH, "//*[contains(@text, \"CONTINUAR\")]")
