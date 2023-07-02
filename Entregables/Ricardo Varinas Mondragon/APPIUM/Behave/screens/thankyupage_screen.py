from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ThankyuScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.lbl_thankyu = (By.XPATH, "//*[contains(@text,'GRACIAS POR SU ORDEN')]")
