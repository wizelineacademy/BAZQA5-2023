from appium.webdriver.common.appiumby import AppiumBy as By

from Behave.extras.base import Actions
from Behave.extras.dictionaries.puchase_confirmation_text import puchase_confirmation


class Success(Actions):
    def init(self, context):
        super().init(context.driver)
        self.message_confirmation = (
            By.ANDROID_UIAUTOMATOR,
            puchase_confirmation.get("message_confirmation"),
        )