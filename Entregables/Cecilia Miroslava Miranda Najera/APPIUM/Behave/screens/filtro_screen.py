from appium.webdriver.common.appiumby import AppiumBy as By
from util.common_actions import CommonActions


class FiltroScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_filtro = (By.XPATH,
                           "//*[@content-desc='test-Modal Selector Button']")
        self.opt_menor_mayor = (By.ANDROID_UIAUTOMATOR,
                                '.text("Price (low to high)")')
        self.max_price = (By.XPATH,
                          "//*[contains(@text, '$49.99')]")
        self.max_product = (By.ANDROID_UIAUTOMATOR,
                            '.text("Sauce Labs Fleece Jacket")')
