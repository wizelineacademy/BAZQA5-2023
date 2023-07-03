from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class PriceFilter(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.tap_filter = (
            By.XPATH, '//android.view.ViewGroup'
                      '[@content-desc="test-Modal Selector Button"]'
                      '/android.view.ViewGroup/android.view.ViewGroup'
                      '/android.widget.ImageView'
        )
        self.tap_low_to_high = (
            By.XPATH, "//*[contains(@text,'Price (low to high)')]"
        )
        self.lbl_lower_price = (
            By.XPATH, "//*[contains(@text,'$7.99')]"
        )
        self.lbl_high_price = (
            By.XPATH, "//*[contains(@text,'$49.99')]"
        )
        self.name_prod = (
            By.XPATH, '//android.widget.ScrollView'
                      '[@content-desc="test-PRODUCTOS"]'
                      '/android.view.ViewGroup/android.view.ViewGroup[3]'
                      '/android.view.ViewGroup/android.widget.TextView[3]'
        )
