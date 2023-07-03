from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH,
                              "//*[contains(@text,'PRODUCTOS')]"
                              )
        self.btn_first_item = (By.ANDROID_UIAUTOMATOR,
                               'text("AÑADIR A CARRITO")'
                               )
        self.icon_cart = (By.ACCESSIBILITY_ID, 'test-Articulo')
        self.lbl_title_item = (By.XPATH,
            "(//*[contains(@content-desc,'test-Descripción')])[1]")
        self.lbl_price_first_item = (By.XPATH,
            "(//*[contains(@content-desc,'test-Precio')])")
        self.icon_car = (By.ACCESSIBILITY_ID, 'test-Carrito')


        # Otros metos de Selectores


        self.product_title = (By.ANDROID_UIAUTOMATOR, 'text("Camisa Sauce Labs Bolt")')
        self.product_price = (By.ANDROID_UIAUTOMATOR, 'text("$15.99")')
