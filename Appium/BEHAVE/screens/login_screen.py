from appium.webdriver.common.appiumby import AppiumBy as By
from BEHAVE.utils.Base_actions import BaseActions


class LoginScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_username = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.txt_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")