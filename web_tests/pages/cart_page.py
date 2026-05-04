from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def finalizar_compra(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")