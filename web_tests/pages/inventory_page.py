from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_primeiro_produto(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
        ).click()

    def ir_para_carrinho(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart")
        )