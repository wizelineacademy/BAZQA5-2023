from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class LoginScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.txt_username = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.txt_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")
        self.login_screen = (
            By.XPATH, '//android.widget.ScrollView'
                      '[@content-desc="test-Login"]'
                      '/android.view.ViewGroup/android.widget.ImageView[1]'
        )
        self.home_page = (
            By.XPATH, '//android.view.ViewGroup'
                      '[@content-desc="test-Zona de caída del carrito de '
                      'compras"]/android.view.ViewGroup'
                      '/android.widget.TextView')
