from appium.webdriver.common.appiumby import AppiumBy as By

from Behave.extras.base import Actions


class Summary(Actions):
    def init(self, context):
        super().init(context.driver)
        self.btn_terminar = (By.ACCESSIBILITY_ID, "test-TERMINAR")