from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.input_data import PRODUCT_TEXTS


class ProductDetailScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        text_title_product_detail = PRODUCT_TEXTS \
            .get("txt_title_product_detail")
        text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
        text_precio_producto = PRODUCT_TEXTS.get("txt_price")
        text_anadir_a_carrito = PRODUCT_TEXTS.get("txt_add_cart")
        content_desc_carrito = PRODUCT_TEXTS.get("contest_desc_cart")
        self.lbl_title_product_detail = (By.XPATH,
                                         '//*[contains(@text,"{}")]'
                                         .format(text_title_product_detail))
        self.scroll_down_product_name = (By.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector().'
                                         'scrollable(true).instance(0)).'
                                         'scrollIntoView(new UiSelector().'
                                         'textContains("{}").instance(0))'
                                         .format(text_nombre_producto))
        self.scroll_down_product_price = (By.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector().'
                                          'scrollable(true).instance(0)).'
                                          'scrollIntoView(new UiSelector().'
                                          'textContains("{}").instance(0))'
                                          .format(text_precio_producto))
        self.scroll_down_product_add_cart = (By.ANDROID_UIAUTOMATOR,
                                             'new UiScrollable('
                                             'new UiSelector().'
                                             'scrollable(true).'
                                             'instance(0)).'
                                             'scrollIntoView('
                                             'new UiSelector().'
                                             'textContains("{}").'
                                             'instance(0))'
                                             .format(text_anadir_a_carrito))
        self.lbl_anadir_a_carrito = (By.XPATH,
                                     '//*[contains(@text,"{}")]'
                                     .format(text_anadir_a_carrito))
        self.opc_carrito = (By.XPATH,
                            '//android.view.ViewGroup[@content-desc="{}"]'
                            .format(content_desc_carrito))
