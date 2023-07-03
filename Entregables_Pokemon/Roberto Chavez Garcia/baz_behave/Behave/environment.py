import subprocess
from os.path import dirname, abspath

from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'R5CW30Z8K9N',
        'app': 'E:\\Users\\1069257\\Documents\\baz_behave\\APP\\sauce_app.apk',
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    context.driver.implicitly_wait(10)

 #Reporte allure
def after_scenario(context, scenario):
    subprocess.run("allure serve reports/android", shell=True)
    context.driver.quit()


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f"{current_directory}/.env")

    context.STANDARD_USER = data["STANDARD_USER"]
    context.PASSWORD = data["PASSWORD"]


def before_all(context):
    context_variables(context)

