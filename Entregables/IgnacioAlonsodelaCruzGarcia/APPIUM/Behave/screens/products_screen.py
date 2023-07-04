from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.input_data import LOGIN_TEXTS, \
    PRODUCT_TEXTS, \
    ORDER_BY_PRICE_TEXTS


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        text_title = LOGIN_TEXTS.get("text_homepage")
        text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
        text_precio_menor = ORDER_BY_PRICE_TEXTS.get("txt_precio_menor")
        text_precio_mayor = ORDER_BY_PRICE_TEXTS.get("txt_precio_mayor")
        self.lbl_productos = (By.XPATH,
                              '//*[contains(@text,"{}")]'
                              .format(text_title))
        self.lbl_nombre_producto = (By.XPATH,
                                    '//*[contains(@text,"{}")]'
                                    .format(text_nombre_producto))
        self.opc_carrito = (By.XPATH,
                            "//android.view.ViewGroup"
                            "[@content-desc=\"test-Carrito\"]")
        self.opc_filtro = (By.XPATH,
                           "//android.view.ViewGroup"
                           "[@content-desc="
                           "\"test-Modal Selector Button\"]")
        self.opc_minor_to_major = (By.XPATH,
                                   '//*[contains(@text, '
                                   '"Price (low to high)")]')
        self.lbl_precio_bajo = (By.XPATH,
                                '//*[contains(@text,"{}")]'
                                .format(text_precio_menor))
        self.scroll_down_precio_alto = (By.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        'scrollIntoView(new UiSelector().'
                                        'textContains("{}").instance(0))'
                                        .format(text_precio_mayor))
        self.lbl_anadir_a_carrito = (By.XPATH,
                                     '//*[contains(@text, '
                                     '"AÑADIR A CARRITO")]')
