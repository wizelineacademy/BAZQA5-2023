import subprocess
from appium import webdriver

def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'JZ6LNZRS6T5TRWZ5',
        'app': '/Users/leticiaquezadacalzada/PycharmProjects/bajar_proyectos/BAZQA5-2023/Entregables/Leticia Quezada Calzada/APPIUM/APP/sauce_app.apk',
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver.implicitly_wait(5)


def after_scenario(context, scenario):
    #subprocess.run("allure serve reports/android", shell=True)
    context.driver.quit()



