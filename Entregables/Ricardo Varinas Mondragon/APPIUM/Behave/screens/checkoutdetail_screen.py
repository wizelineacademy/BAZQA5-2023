from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CheckoutDetailScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.btn_finish = (By.ACCESSIBILITY_ID, "test-TERMINAR")
