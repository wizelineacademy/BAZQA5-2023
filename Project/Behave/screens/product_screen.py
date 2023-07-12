from appium.webdriver.common.appiumby import AppiumBy as By
from utils.Base_actions import BaseActions



class ProductosScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.ANDROID_UIAUTOMATOR, '.text("PRODUCTS")')
        self.btn_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-ADD TO CART')])[1]",)
        self.lbl_title_item = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Backpack")')
        self.icon_car = (By.XPATH, "//*[contains(@content-desc,'test-Cart')]")
        self.price_first_item = (By.ANDROID_UIAUTOMATOR, '.text("$29.99")')
        self.icon_filter = (By.ACCESSIBILITY_ID, "test-Modal Selector Button")
        self.option_lowest_to_highest = (By.ANDROID_UIAUTOMATOR, '.text("option_lowest_to_highest")')
        self.higher_product_price = (By.ANDROID_UIAUTOMATOR, '.text("higher_product_price")')
        self.higher_product_name = (By.ANDROID_UIAUTOMATOR, '.text("higher_product_name")')
        self.Producto_1_IMG = (By.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])[1]')