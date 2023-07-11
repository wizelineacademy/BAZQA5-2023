from appium.webdriver.common.appiumby import AppiumBy as By

from BEHAVE.utils.Base_actions import BaseActions


class Resumen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_terminar = (By.ACCESSIBILITY_ID, "test-TERMINAR")