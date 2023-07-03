from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (
            By.XPATH, "//*[contains(@text,'PRODUCTOS')]"
        )
        self.tap_product = (
            By.XPATH, '(//android.view.ViewGroup'
                      '[@content-desc="test-Articulo"])[1]'
                      '/android.view.ViewGroup'
                      '/android.widget.ImageView')

        self.product_price = (
            By.ACCESSIBILITY_ID, 'test-Precio'
        )
        self.product_name = (
            By.XPATH, "//*[contains(@text,'Camisa Sauce Labs Bolt')]"
        )
