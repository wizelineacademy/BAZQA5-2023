from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CartScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.cart_title_item = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]/android.widget.TextView[1]")
        self.cart_description_item = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]/android.widget.TextView[2]")
        self.cart_price_item = (By.XPATH, "//*[contains(@content-desc, 'test-Precio')]/android.widget.TextView")
        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")
