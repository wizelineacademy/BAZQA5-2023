from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class BuyProductsScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_add = (By.XPATH, "(//*[@content-desc='test-AÑADIR A CARRITO'])")
        self.lbl_kart = (By.XPATH, "(//*[@content-desc='test-Carrito'])")
        self.lbl_remove = (By.XPATH, "//*[contains(@text,'REMOVER')]")
        self.lbl_buy_more = (By.XPATH, "//*[contains(@text,'CONTINUAR COMPRANDO')]")


