from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class LoginScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_username = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.txt_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")
