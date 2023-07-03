from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.cart_screenstext import product_detail_screen


class CartScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")
        self.header_title = (By.ANDROID_UIAUTOMATOR,
                             product_detail_screen.get("header_title")
                             )
        self.ProductName = (By.ANDROID_UIAUTOMATOR,
                            product_detail_screen.get("ProductName")
                            )
        self.ProductPrice = (By.ANDROID_UIAUTOMATOR,
                             product_detail_screen.get("ProductPrice")
                             )
        self.ProductDescription = (By.ANDROID_UIAUTOMATOR,
                                   product_detail_screen.get("ProductDescription")
                                  )

