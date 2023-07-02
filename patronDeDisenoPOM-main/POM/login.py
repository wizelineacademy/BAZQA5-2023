# Esto lo utilizamos para poder selecionar nuestros elementos

from appium.webdriver.common.appiumby import AppiumBy as By
from utilities.commonMethods import BaseClass

class LoginPage(BaseClass):


    ####
    # Los selectores van aqui como variables
    ####
    def __init__(self, driver):
        super().__init__(driver)
        self.txtusername = (By.XPATH, '//android.widget.EditText[@content-desc="test-Usuario"]')
        self.txtpassword = (By.XPATH, '//android.widget.EditText[@content-desc="test-Contraseña"]')
        self.btn_login = (By.ACCESSIBILITY_ID, 'test-LOGIN')
        self.lbl_mensaje_error = (By.ANDROID_UIAUTOMATOR, '.text("Provided credentials do not match any user in this service.")')
        self.lbl_mensaje_username_req = (By.ACCESSIBILITY_ID, "test-Error")

    ####
    # Los metodos / acciones de pagina especifica van aqui
    # El constructor viene de la clase padre
    # Podemos usar el driver aqui con self.driver
    # Podemos llamar a los metodos de BaseClass por la herencia como self.nombre_metodo_de_BaseClass
    #
    ####

    def set_username(self, username):
        self.driver.
        valor = self.driver.find_element(*self.txtusername).send_keys(username)
        return valor

    def set_password(self, password):
        valor = self.driver.find_element(*self.txtpassword).send_keys(password)
        return  valor

    def click_login(self):
        self.driver.find_element(*self.btn_login).click()
