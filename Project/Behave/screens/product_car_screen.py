from appium.webdriver.common.appiumby import AppiumBy as By
from utils.Base_actions import BaseActions



class ProductCar(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.XPATH, '//android.view.ViewGroup[@content-desc="test-Description"]/android.widget.TextView[1]',)
        self.price_first_item_cart = (By.ACCESSIBILITY_ID, '//android.view.ViewGroup[@content-desc="test-Price"]/android.widget.TextView',)
        self.btn_checkout = (By.ACCESSIBILITY_ID, 'test-CHECKOUT')
        self.lbl_tu_carrito = (By.ANDROID_UIAUTOMATOR, '.text("LABELCAR")')