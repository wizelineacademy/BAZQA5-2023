from appium.webdriver.common.appiumby import AppiumBy as By
from utils.Base_actions import BaseActions


class Checkout(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.txt_name = (By.ACCESSIBILITY_ID, "test-First Name")
        self.txt_apellido = (By.ACCESSIBILITY_ID, "test-Last Name")
        self.txt_codigopostal = (By.ACCESSIBILITY_ID, "test-Zip/Postal Code")
        self.btn_continuar = (By.ACCESSIBILITY_ID, "test-CONTINUE")