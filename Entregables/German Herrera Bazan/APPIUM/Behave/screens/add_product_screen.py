from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class AddProduct(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.add_producto = (
            By.XPATH, '(//android.view.ViewGroup'
                      '[@content-desc="test-AÑADIR A CARRITO"])[2]'
        )
        self.tap_cart = (
            By.XPATH, '//android.view.ViewGroup[@content-desc="test-Carrito"]'
                      '/android.view.ViewGroup/android.view.ViewGroup'
        )
        self.lbl_price_product = (
            By.XPATH, '//android.view.ViewGroup'
                      '[@content-desc="test-Precio"]'
                      '/android.widget.TextView'
        )
        self.lbl_name_product = (
            By.XPATH, "//*[contains(@text,'Camisa "
                      "Test.allTheThings() (Roja)')]"
        )
        self.lbl_description_product = (
            By.XPATH, "//*[contains(@text,'This classic Sauce Labs "
                      "t-shirt is perfect to wear when cozying up to "
                      "your keyboard to automate a few tests. Super-soft "
                      "and comfy ringspun combed cotton.')]"
        )
        self.lbl_title_item = (
            By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]"
                      "/android.widget.TextView[1]"
        )
