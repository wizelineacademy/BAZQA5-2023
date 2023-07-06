from appium.webdriver.common.appiumby import AppiumBy as By

from Behave.extras.base import Actions


class Login(Actions):
    def init(self, context):
        super().init(context.driver)
        self.txt_username = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.txt_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")