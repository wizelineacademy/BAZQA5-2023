from utils.dictionaries.coordenadas import Coordenadas
from appium.webdriver.common.touch_action import TouchAction


class CommonActions(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def assert_text(self, *locator, text):
        element_text = self.find_element(*locator).text
        assert element_text == text

    def tap_element(self, *locator):
        action = TouchAction(self.driver)
        action.tap(self.find_element(*locator)).perform()

    def fill_text(self, *locator, text):
        text_field = self.find_element(*locator)
        text_field.send_keys(text)

    def get_text_of_element(self, *locator):
        return self.driver.find_element(*locator).text

    def scroll_down(self, *locator):
        for _ in range(Coordenadas.get("MAX_NUM_OF_SWIPES")):
            try:
                self.find_element(*locator)
                break
            except:
                touch = TouchAction(self.driver)
                touch.press(None, Coordenadas.get('X_START'), Coordenadas.get('Y_START')) \
                    .wait(Coordenadas.get('TIME_TO_WAIT')) \
                    .move_to(None, Coordenadas.get('X_END'), Coordenadas.get('Y_END')) \
                    .release().perform()
