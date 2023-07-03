from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class CheckoutResumenScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_terminar = (By.XPATH, "//*[contains(@text, \"TERMINAR\")]")
