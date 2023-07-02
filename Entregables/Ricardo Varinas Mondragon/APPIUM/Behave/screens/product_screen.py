from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH, "//*[contains(@text,'PRODUCTOS')]")
        self.btn_addcarrito = (By.XPATH, "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]")
        self.img_prod_item = (By.XPATH, "(//*[contains(@content-desc,'test-Articulo')])[1]")
        self.lbl_title_item = (By.XPATH, "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]")
        self.lbl_price_item = (By.XPATH, "(//*[contains(@content-desc,'test-Precio')])[1]")
        self.icon_car = (By.XPATH, "//*[contains(@content-desc,'test-Carrito')]")
        self.btn_filter = (By.XPATH, "//*[contains(@content-desc,'test-Modal Selector Button')]")
        self.btn_sortitem = (By.XPATH, "//*[contains(@text,'Price (low to high)')]")

        self.lbl_price_low = (By.XPATH, "(//*[contains(@content-desc,'test-Precio')])[1]")
        self.lbl_price_high = (By.XPATH, "(//*[contains(@content-desc,'test-Precio')])[2]")

        self.btn_addcarrito_firstitem = (By.XPATH, "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]")
        self.btn_addcarrito_seconditem = (By.XPATH, "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]")
