from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def fazer_login(self, usuario, senha):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        ).send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(senha)
        self.driver.find_element(By.ID, "login-button").click()

        # Aguarda confirmar que o login funcionou
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory")
        )