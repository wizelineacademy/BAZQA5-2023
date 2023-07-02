from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.utils.common_actions import CommonActions
from utils.dictionaries.product_cart_screen import cart_screen


class CarritoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.ANDROID_UIAUTOMATOR, cart_screen.get("ProductName"))
        self.price_first_item_cart = (By.ANDROID_UIAUTOMATOR, cart_screen.get("ProductPrice"))
        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")