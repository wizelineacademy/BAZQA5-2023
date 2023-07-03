import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("STANDARD_USER")
password = os.getenv("PASSWORD")

LOGIN_TEXTS = {
    'txt_username': "standard_user",
    'txt_password': "secret_sauce"
}

PRODUCT_TEXTS = {
    'PRODUCT_PAGE': "PRODUCTOS"
}
