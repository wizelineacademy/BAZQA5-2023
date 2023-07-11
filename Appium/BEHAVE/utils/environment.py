from os.path import dirname, abspath
from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        "platformName": "android",
        "platformVersion": "10",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity",
        "appName": "Swag Labs Mobile App"
    }

    context.driver.implicitly_wait(10)


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f'{current_directory}/.env')

    context.STANDARD_USER = data['STANDARD_USER']
    context.PASSWORD = data['PASSWORD']
    context.ERROR_USER = data['ERROR_USER']
    context.ERROR_PASS = data['ERROR_PASS']
    context.PROD_HIGH_NAME = data['PROD_HIGH_NAME']
    context.PROD_HIGH_PRICE = data['PROD_HIGH_PRICE']
    context.PROD_LOW_NAME = data['PROD_LOW_NAME']
    context.PROD_LOW_PRICE = data['PROD_LOW_PRICE']
    context.BTN_LOGIN = data['test-LOGIN']
    context.FIRST_ELEMENT = data['Sauce Labs Bike Light']


def before_all(context):
    context_variables(context)


def after_all(context):
    subprocess.run("allure serve reports/android", shell=True)