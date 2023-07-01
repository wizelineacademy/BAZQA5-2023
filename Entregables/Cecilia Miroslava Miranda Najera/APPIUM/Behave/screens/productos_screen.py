from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions

class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH, "//*[contains(@text,'PRODUCTS')]")
        self.btn_add = (By.XPATH, "(//*[@content-desc='test-ADD TO CART'])[2]")
        self.btn_car = (By.XPATH, "(//*[@content-desc = 'test-Cart'])")
        self.nombre_producto = (By.XPATH, "//*[contains(@text, 'Sauce Labs Bike Light')]")
        self.precio_producto = (By.XPATH, "//*[contains(@text, '$9.99')]")
