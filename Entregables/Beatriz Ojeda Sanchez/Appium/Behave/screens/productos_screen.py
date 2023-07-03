from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.extras.base import Actions
from Behave.extras.dictionaries.productos_screen_text import product_screen


class Prod(Actions):
    def init(self, context):
        super().init(context.driver)
        self.lbl_productos = (By.ANDROID_UIAUTOMATOR, '.text("PRODUCTOS")')
        self.btn_first_item = (
            By.XPATH,
            "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]",
        )
        self.lbl_title_item = (
            By.XPATH,
            "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]",
        )
        self.icon_car = (By.XPATH, "//*[contains(@content-desc,'test-Carrito')]")
        self.price_first_item = (
            By.XPATH,
            '(//*[contains(@content-desc,"test-Precio")])[1]',
        )
        self.icon_filter = (
            By.XPATH,
            "(//*[contains(@content-desc,'test-Modal Selector Button')])[1]",
        )
        self.option_lowest_to_highest = (
            By.ANDROID_UIAUTOMATOR,
            product_screen.get("option_lowest_to_highest"),
)
        self.higher_product_price = (
            By.ANDROID_UIAUTOMATOR,
            product_screen.get("higher_product_price"),
        )
        self.higher_product_name = (
            By.ANDROID_UIAUTOMATOR,
            product_screen.get("higher_product_name"),
        )
        self.Producto_1_IMG = (By.XPATH, '(//android.view.ViewGroup[@content-desc="test-Articulo"])[1]')