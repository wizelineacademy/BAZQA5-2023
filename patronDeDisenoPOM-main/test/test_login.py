import pytest
from POM.login import LoginPage
from dotenv import load_dotenv
from POM.home import  HomePage
from conftest import driver_setup
import os


# Usamos fixture para iniciar el server de appium, solo se llama una vez en el archivo
#@pytest.mark.usefixtures("appium_start")
class TestSignIn:


    load_dotenv("..\\utilities\\.env")
    ####
    # Aqui van los test cases de la suite
    ####

    ####
    # Uso driver_setup como Arrange y cleanup
    #def test_login_user_with_issues(self, driver, user, password, errormsg):
    #    Act
    #   Assert
    ####
    @pytest.mark.smoke
    def test_login_valido(self, driver_setup):
        #username = os.getenv("STANDARD_USER")
        #password = os.getenv("PASSWORD")
        username = "standard_user"
        password = "secret_sauce"
        print("username", username)
        home_page = HomePage(driver_setup)

        login_page = LoginPage(driver_setup)
        assert login_page.set_username(username) == username
        assert login_page.set_password(password) == password        
        #login_page.click_login()



        #assert home_page.wait_for_element(*home_page.lbl_products)

