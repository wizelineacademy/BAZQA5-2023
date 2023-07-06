from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.extras.base import Actions
from Behave.extras.dictionaries.product_car_screen_text import car_screen

class Product(Actions):
    def init(self, context):
        super().init(context.driver)
        self.lbl_title_first_item_cart = (By.ANDROID_UIAUTOMATOR, car_screen.get("NAMEPRODUCT"))
        self.price_first_item_cart = (By.ANDROID_UIAUTOMATOR, car_screen.get("PRICEPRODUCT"))
        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")
        self.lbl_tu_carrito = (By.ANDROID_UIAUTOMATOR, car_screen.get("LABELCAR"))