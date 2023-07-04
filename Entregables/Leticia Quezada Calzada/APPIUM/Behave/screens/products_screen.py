from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH, "//*[contains(@text,'PRODUCTOS')]")
        self.lbl_name_product = (By.XPATH, "//*[contains(@text,'Chamarra Sauce Labs')]")
        self.lbl_price_product = (By.XPATH, "//*[contains(@text,'$49.99')]")

