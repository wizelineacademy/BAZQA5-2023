from appium.webdriver.common.touch_action import TouchAction
from time import sleep

from utils.dictionaries.swipe_properties_texts import COORDINATES
from selenium.webdriver.support import expected_conditions as EC


class CommonActions(object):

    def __init__(self, driver):
        self.driver = driver
        self.screen_width = None
        self.screen_height = None

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

    def find_and_click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def scroll(self, *locator):
        for _ in range(COORDINATES.get('MAX_NUM_OF_SWIPES')):
            try:
                self.find_and_click_element(*locator)
                break
            except ValueError:
                self.driver.swipe(COORDINATES.get('X_START'),
                                  COORDINATES.get('X_END'),
                                  COORDINATES.get('Y_START'),
                                  COORDINATES.get('Y_END'),
                                  COORDINATES.get('TIME_TO_WAIT'))
                continue

    def scroll_to_element(self, x0, y0, x1, y1, locator):
        # Este numero va acorder a nustras necesidades
        for _ in range(10):
            try:
                if self.find_element(locator).is_displayed():
                    # Para debugear
                    print("Element found")
                    sleep(10)
                    ######
                    break
            except ValueError:
                self.driver.swipe(x0, y0, x1, y1)
                sleep(3)
                continue

    def scroll1(self, *locator):
        for _ in range(COORDINATES.get("MAX_NUM_OF_SWIPES")):
            try:
                self.find_element(*locator)
                break
            except ValueError:
                self.driver.swipe(
                    COORDINATES.get("X_START"),
                    COORDINATES.get("X_END"),
                    COORDINATES.get("Y_START"),
                    COORDINATES.get("Y_END"),
                    COORDINATES.get("TIME_TO_WAIT"),
                )
                continue

    def get_window_size(self):
        if self.screen_width is None or self.screen_height is None:
            window_size = self.driver.get_window_size()
            self.screen_width = window_size['width']
            self.screen_height = window_size['height']

    def scroll_down(self):
        self.get_window_size()

        # Calcular las coordenadas para el scroll
        start_x = self.screen_width // 2
        start_y = int(self.screen_height * 0.8)
        end_y = int(self.screen_height * 0.2)
        sleep(3)
        # Realizar el scroll utilizando el método swipe()
        self.driver.swipe(start_x, start_y, start_x, end_y, 400)

    def wait_element_to_be_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))
