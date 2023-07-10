from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.ANDROID_UIAUTOMATOR, '.text("PRODUCTS")')
        self.btn_Add_Cart = (By.XPATH, "//*[contains(@text,'ADD TO CART')]")
        self.icon_cart = (By.ACCESSIBILITY_ID, "test-Cart")
        self.detail_product = (By.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])[1]' '/android.view.ViewGroup/android.widget.ImageView')
        self.lbl_price = (By.ANDROID_UIAUTOMATOR, '.text("$29.99")')
        self.lbl_product_name = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Backpack")')