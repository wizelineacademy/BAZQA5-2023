from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ItemScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.lbl_item_single_title = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]/android.widget.TextView[1]")
        self.lbl_item_single_price = (By.ACCESSIBILITY_ID, "test-Precio")
        self.lbl_item_description = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]/android.widget.TextView[2]")
        self.btn_addcarrito_item = (By.ACCESSIBILITY_ID, "test-AÑADIR A CARRITO")
        self.btn_cart = (By.XPATH, "//*[contains(@content-desc,'test-Carrito')]")
