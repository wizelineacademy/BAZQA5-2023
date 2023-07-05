from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions

class CarritoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.btn_Add_Cart = (By.XPATH, "//*[contains(@text,'ADD TO CART')]")
        self.icon_cart = (By.ACCESSIBILITY_ID, "test-Cart")
        self.lbl_title_cart = (By.ACCESSIBILITY_ID, "DESCRIPTION")
        self.lbl_price_cart = (By.ANDROID_UIAUTOMATOR, '.text("$29.99")')
        self.lbl_product_name_cart = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Backpack")')






