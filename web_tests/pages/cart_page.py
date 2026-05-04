from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def finalizar_compra(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # Aguarda confirmar que entrou no checkout
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one")
        )