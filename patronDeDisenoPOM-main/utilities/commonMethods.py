import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BaseClass:

    # Constructor de nuestra clase
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    # Esperamos que elemento este presente en el DOM y lo retornamos - explicit wits
    def wait_for_element(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    # Esperamos que un elemento este visible y lo retornamos - explicit waits
    def wait_element_to_be_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    # Buscamos y retornamos cierto elemento - aqui usamos el * para mandarlo como 2 argumentos
    def find(self, locator):
        return self.driver.find_element(*locator)

    # Hacemos scroll hasta ubicar x elemento
    def scroll_to_element(self, x0, y0, x1, y1, locator):
        # Este numero va acorder a nustras necesidades
        for _ in range(10):
            try:
                if (self.find(locator).is_displayed()):
                    # Para debugear
                    print("Element found")
                    sleep(10)
                    ######
                    break
            except:
                self.driver.swipe(x0, y0, x1, y1)
                sleep(3)
                continue