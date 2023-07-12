from appium.webdriver.common.appiumby import AppiumBy as By
from utils.Base_actions import BaseActions


class LoginScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_username = (By.ACCESSIBILITY_ID, "test-Username")
        self.txt_password = (By.ACCESSIBILITY_ID, "test-Password")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")