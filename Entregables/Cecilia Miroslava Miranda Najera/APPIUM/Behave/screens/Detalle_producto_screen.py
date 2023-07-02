from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class DetalleProductoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.select_producto = (By.XPATH,
                                '(//*[@content-desc="test-Item"])[1]/android.view.ViewGroup/android.widget.ImageView')
        self.desc_producto = (By.XPATH,
                              "//*[contains(@text, 'Sauce Labs Backpack')]")
        self.price_producto = (By.XPATH, "//*[contains(@text, '$29.99')]")
