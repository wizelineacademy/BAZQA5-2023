import subprocess
from os.path import dirname, abspath
from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:app": "/Users/1055283/PycharmProjects/Project/APP/sauce_app.apk",
        "appium:automationName": "UiAutomator2",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:appPackage": "com.swaglabsmobileapp"
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                      desired_caps
                                      )
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    subprocess.run("allure serve reports/android", shell=True)
    context.driver.quit()


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f'{current_directory}/.env')
    context.PROD = data['PROD']
    context.PRICE = data['PRICE']
    context.PRODUCTOS = data['PRODUCTOS']
    context.HOME = data['PRODUCTOS']
    context.PROD_HIGH_NAME = data['PROD_HIGH_NAME']
    context.PROD_HIGH_PRICE = data['PROD_HIGH_PRICE']
    context.PROD_LOW_NAME = data['PROD_LOW_NAME']
    context.PROD_LOW_PRICE = data['PROD_LOW_PRICE']


def before_all(context):
    context_variables(context)
