from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.extras.base import Actions


class Check(Actions):
    def init(self, context):
        super().init(context.driver)

        self.txt_name = (By.ACCESSIBILITY_ID, "test-Nombre")
        self.txt_apellido = (By.ACCESSIBILITY_ID, "test-Apellido")
        self.txt_codigopostal = (By.ACCESSIBILITY_ID, "test-Código postal")
        self.btn_continuar = (By.ACCESSIBILITY_ID, "test-CONTINUAR")