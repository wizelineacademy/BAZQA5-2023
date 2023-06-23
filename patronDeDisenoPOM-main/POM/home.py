# Esto lo utilizamos para poder selecionar nuestros elementos

from appium.webdriver.common.appiumby import AppiumBy as By
from utilities.commonMethods import BaseClass


# Esta clase herada lo que tenemos en la clase base
class HomePage(BaseClass):


    ######
    # Los selectores van aqui como variables
    ####
    def __init__(self,driver):
        super().__init__(driver)
        self.btn_menu = (By.XPATH, "android.view.ViewGroup/android.widget.ImageView")
        self.lbl_products = (By.ANDROID_UIAUTOMATOR, '.text("PRODUCTOS)')

    ####
    # Los metodos / acciones de pagina especifica van aqui
    # El constructor viene de la clase padre
    # Podemos usar el driver aqui con self.driver
    # Podemos llamar a los metodos de BaseClass por la herencia como self.nombre_metodo_de_BaseClass
    #
    ####

    def ir_login(self):
        pass
        #self.driver.find_element(*self.btn_menu).click()
        #self.driver.find_element(*self.lbl_products).click()

