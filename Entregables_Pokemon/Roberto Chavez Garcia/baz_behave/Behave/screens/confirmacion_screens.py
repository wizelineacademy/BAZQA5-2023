from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.confirmacion_text import confirma


class Confirmation(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.message_confirmation = (
            By.ANDROID_UIAUTOMATOR,
            confirma.get("message_confirmation"))
