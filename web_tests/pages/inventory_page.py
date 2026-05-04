from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_primeiro_produto(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        self.driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    def ir_para_carrinho(self):
        self.driver.get("https://www.saucedemo.com/cart.html")