import subprocess
from os.path import dirname, abspath
from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        "platformName": "Android",
         "appium:deviceName": "8bc43896",
         "appium:app": "E:\\Desarrollos\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
         "appium:automationName": "uiautomator2",
         "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
         "appPackage": "com.swaglabsmobileapp"
}
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    context.driver.implicitly_wait(10)


def after_all(context):
    subprocess.run("allure serve reports/android", shell=True)
    context.driver.quit()

def context_variables(context):
    current_directory = dirname(abspath(file))
    data = dotenv_values(f"{current_directory}/.env")

    context.STANDARD_USER = data["STANDARD_USER"]
    context.PASSWORD = data["PASSWORD"]


def before_all(context):
    context_variables(context)