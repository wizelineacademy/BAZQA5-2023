from appium.webdriver.common.appiumby import AppiumBy as By

from utils.Base_actions import BaseActions


class PurchaseConfirmation(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.message_confirmation = (By.ANDROID_UIAUTOMATOR, '.text("message_confirmation")')
