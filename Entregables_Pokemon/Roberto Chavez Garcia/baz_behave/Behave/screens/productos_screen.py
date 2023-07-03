from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions
from utils.dictionaries.Products_screen import productScreen

class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (
            By.XPATH,
            "//*[contains(@text,'PRODUCTOS')]")
        self.btn_first_item = (
            By.ANDROID_UIAUTOMATOR,
            'text("AÑADIR A CARRITO")')
        self.icon_cart = (By.XPATH, "//*[contains(@content-desc,'test-Carrito')]")
        self.lbl_title_item = (
            By.XPATH,
            "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]")
        self.price_first_item = (
            By.XPATH,
            "(//*[contains(@content-desc,'test-Precio')])[1]")
        self.Producto_1_IMG = (
            By.XPATH,
            '(//android.view.ViewGroup[@content-desc="test-Articulo"])[1]')
        self.icon_filter = (
            By.XPATH,
            "(//*[contains(@content-desc, 'test-Modal Selector Button')])[1]",
        )
        self.option_lowest_to_highest = (
            By.ANDROID_UIAUTOMATOR,
            productScreen.get("option_lowest_to_highest"),
        )
        self.higher_product_name = (
            By.ANDROID_UIAUTOMATOR,
            productScreen.get("higher_product_name"),
        )
        self.higher_product_price = (
            By.ANDROID_UIAUTOMATOR,
            productScreen.get("higher_product_price"),
        )