from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class FilterScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.icon_filter = (By.ACCESSIBILITY_ID,
                            "test-Modal Selector Button")
        self.lbl_max_price = (By.ANDROID_UIAUTOMATOR,
                              'text("Price (high to low)")')
        self.max_product_title = (By.ANDROID_UIAUTOMATOR,
                                  'text("Chamarra Sauce Labs")')
        self.max_product_price = (By.ANDROID_UIAUTOMATOR,
                                  'text("$49.99")')
        self.lbl_min_price = (By.ANDROID_UIAUTOMATOR,
                              'text("Price (low to high)")')
        self.min_product_title = (By.ANDROID_UIAUTOMATOR,
                                  'text("Mameluco Sauce Labs")')
        self.min_product_price = (By.ANDROID_UIAUTOMATOR,
                                  'text("$7.99")')
