from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class FilterScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_filter = (By.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]/' 'android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
        self.btn_low_price = (By.ANDROID_UIAUTOMATOR, '.text("Price (low to high)")')
        self.btn_high_price = (By.ANDROID_UIAUTOMATOR, '.text("Price (high to low)")')
        self.lbl_low_price_item = (By.ANDROID_UIAUTOMATOR, '.text("$7.99")')
        self.lbl_high_price_item = (By.ANDROID_UIAUTOMATOR, '.text("$49.99")')
