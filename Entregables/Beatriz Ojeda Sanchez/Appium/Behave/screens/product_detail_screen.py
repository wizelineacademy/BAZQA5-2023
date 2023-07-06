from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.extras.base import Actions
from Behave.extras.dictionaries.product_detail_screen_text import product_detail_screen


class Details(Actions):
    def init(self, context):
        super().init(context.driver)
        self.header_title = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("header_title"))
        self.ProductName = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("ProductName"))
        self.ProductPrice = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("ProductPrice"))
        self.ProductDescription = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("ProductDescription"))