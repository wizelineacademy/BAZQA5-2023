import subprocess
from os.path import dirname, abspath
from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': '/Users/cmirandan/Documents/GitHub/BAZQA5-2023/Entregables/Cecilia Miroslava Miranda Najera/APPIUM/APP/sauce_app.apk',
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver.implicitly_wait(10)


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f'{current_directory}/.env')

    context.STANDARD_USER = data['STANDARD_USER']
    context.PASSWORD = data['PASSWORD']


def before_all(context):
    context_variables(context)


def after_scenario(context, scenario):
    #subprocess.run("allure serve reports/android", shell=True)
    context.driver.quit()



