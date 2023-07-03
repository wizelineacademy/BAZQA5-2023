from appium.webdriver.common.appiumby import AppiumBy
from utils.common_actions import CommonActions


class LoginScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_username = (AppiumBy.ACCESSIBILITY_ID, "test-Usuario")
        self.txt_password = (AppiumBy.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
