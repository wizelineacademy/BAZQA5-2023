from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.input_data import PRODUCT_TEXTS, CART_TEXTS


class ShoppingCartScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        text_titulo_tu_carrito = CART_TEXTS.get("txt_title_cart")
        text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
        text_precio_producto = PRODUCT_TEXTS.get("txt_price")
        self.title_tu_carrito = (By.XPATH, '//*[contains(@text,"{}")]'
                                 .format(text_titulo_tu_carrito))
        self.lbl_nombre_producto = (By.XPATH,
                                    '//*[contains(@text,"{}")]'
                                    .format(text_nombre_producto))
        self.lbl_precio_producto = (By.XPATH, '//*[contains(@text,"{}")]'
                                    .format(text_precio_producto))
