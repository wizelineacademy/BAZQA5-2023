from appium import webdriver


def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '56295fdf',
        'app': 'e:/Users/948255/Documents/'
               'CursoWizelineAutomation/'
               'Entregables/APPIUM/APP/'
               'sauce_app.apk',
        'appPackage': 'com.swaglabsmobileapp',
        'appActivity': '.MainActivity'
    }
    context.driver = webdriver.Remote(
        'http://localhost:4723/wd/hub',
        desired_caps)
    context.driver.implicitly_wait(20)


def after_scenario(context, scenario):
    # subprocess.run("allure serve reports/android", shell=True)
    context.driver.quit()
