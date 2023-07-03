from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions
from utils.dictionaries.input_data import CHECKOUT_TEXTS


class CheckoutCompletadoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        text_title = CHECKOUT_TEXTS.get("txt_title_checkout_terminado")
        text_gracias = CHECKOUT_TEXTS.get("txt_gracias")
        self.lbl_title = (By.XPATH,
                          '//*[contains(@text, "{}")]'
                          .format(text_title))
        self.lbl_gracias = (By.XPATH,
                            '//*[contains(@text, "{}")]'
                            .format(text_gracias))
