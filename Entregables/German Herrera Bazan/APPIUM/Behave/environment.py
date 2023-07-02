import subprocess
from appium import webdriver


def before_scenario(context, scenario):
    desired_caps = {
        "appium:platformName": "Android",
        "appium:deviceName": "ZY22DZ7KJP",
        "appium:app": "E:\\Users\\314511\\PycharmProjects\\baz_behave\\APP\\sauce_app.apk",
        "appium:automationName": "uiautomator2",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity"
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver.implicitly_wait(20)


def after_scenario(context, scenario):
    context.driver.quit()


def after_all(context):
    #  Para ejecutar el reporte Allure
    subprocess.run("allure serve E:/Users/314511/PycharmProjects/baz_behave/Behave/reports/android", shell=True)
