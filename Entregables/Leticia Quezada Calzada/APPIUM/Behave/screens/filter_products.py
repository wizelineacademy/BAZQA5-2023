from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions

class FilterProductsScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_filtro = (By.XPATH, "(//*[@content-desc='test-Modal Selector Button'])")
        self.lbl_order = (By.XPATH, "//*[contains(@text,'Price (low to high)')]")
        self.lbl_name_product = (By.XPATH, "//*[contains(@text,'Chamarra Sauce Labs')]")
        self.lbl_high_product = (By.XPATH, "//*[contains(@text,'$49.99')]")