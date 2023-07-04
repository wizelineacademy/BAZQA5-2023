from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy as By


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

    def scroll_into_element_tap(self, text):
        scroll_down_selector = (By.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().'
                                'scrollable(true).instance(0)).'
                                'scrollIntoView(new UiSelector().'
                                'textContains("{}").instance(0))'
                                .format(text))
        self.tap_element(*scroll_down_selector)

    def scroll_into_element(self, text):
        scroll_down_selector = (By.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().'
                                'scrollable(true).instance(0)).'
                                'scrollIntoView(new UiSelector().'
                                'textContains("{}").instance(0))'
                                .format(text))
        self.find_element(*scroll_down_selector)
