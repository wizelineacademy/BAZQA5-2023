from appium.webdriver.common.touch_action import TouchAction
from utils.dictionaries.swipe_text import COORDINATES

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

    def get_text_of_element(self, *locator,):
        return self.driver.find_element(*locator).text

    def scroll1(self, *locator):
        for _ in range(COORDINATES.get("MAX_NUM_OF_SWIPES")):
            try:
                self.find_element(*locator)
                break
            except:
                self.driver.swipe(
                    COORDINATES.get("X_START"),
                    COORDINATES.get("X_END"),
                    COORDINATES.get("Y_START"),
                    COORDINATES.get("Y_END"),
                    COORDINATES.get("TIME_TO_WAIT"),
                )
                continue
