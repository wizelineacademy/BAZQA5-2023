from appium.webdriver.common.appiumby import AppiumBy as By
from BEHAVE.utils.Base_actions import BaseActions



class ProductCar(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.ANDROID_UIAUTOMATOR, '.text("NAMEPRODUCT")')
        self.price_first_item_cart = (By.ANDROID_UIAUTOMATOR, '.text("PRICEPRODUCT")')
        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")
        self.lbl_tu_carrito = (By.ANDROID_UIAUTOMATOR, '.text("LABELCAR")')