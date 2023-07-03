from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.product_detail_screen import Productdetail_screen


class Product_Detail(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.header_title = (By.ANDROID_UIAUTOMATOR, Productdetail_screen.get("header_title"))
        self.ProductName = (By.ANDROID_UIAUTOMATOR, Productdetail_screen.get("ProductName"))
        self.ProductPrice = (By.ANDROID_UIAUTOMATOR, Productdetail_screen.get("ProductPrice"))
        self.ProductDescription = (By.ANDROID_UIAUTOMATOR, Productdetail_screen.get("ProductDescription"))