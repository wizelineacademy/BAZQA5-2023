from appium.webdriver.common.appiumby import AppiumBy as By
from BEHAVE.utils.Base_actions import BaseActions



class ProductDetail(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.header_title = (By.ANDROID_UIAUTOMATOR, '.text("header_title")')
        self.ProductName = (By.ANDROID_UIAUTOMATOR, '.text("ProductName")')
        self.ProductPrice = (By.ANDROID_UIAUTOMATOR, '.text("ProductPrice")')
        self.ProductDescription = (By.ANDROID_UIAUTOMATOR, '.text("ProductDescription")')