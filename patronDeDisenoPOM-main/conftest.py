import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def driver_setup(request):
    # Desire capabilities section
    #desired_cap = {
    #    "platformName": "android",
    #    "platformVersion": "10",
    #    "deviceName": "emulator-5554",
    #    "automationName": "UiAutomator2",
    #    "appPackage": "com.swaglabsmobileapp",
    #    "appActivity": ".MainActivity"
    #}

    desired_cap = {
        "platformName": "Android",
        "appium:deviceName": "ZY22DZ7KJP",
        "appium:app": "E:\\Users\\314511\\PycharmProjects\\patronDeDisenoPOM-main\\others\\saucedemo.apk",
        "appium:automationName": "uiautomator2",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity"
    }

    # Creating the driver by passing the desired capabilities
    #driver = webdriver.Remote("http://0.0.0.0:4723", desired_cap)
    request.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield request.driver
    print("Closing the driver")
    request.driver.quit()

"""
#@pytest.fixture(scope="module")
#def appium_start():
 #   appium_service = AppiumService()
  #  print("Start appium server")
   # appium_service.start()
   # yield
    print("Stop appium server")
    appium_service.stop()

"""