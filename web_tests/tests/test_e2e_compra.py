from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_fluxo_completo_de_compra(driver):
    # Login
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("standard_user", "secret_sauce")

    # Adicionar produto ao carrinho
    inventory = InventoryPage(driver)
    inventory.adicionar_primeiro_produto()
    inventory.ir_para_carrinho()

    # Finalizar compra
    cart = CartPage(driver)
    cart.finalizar_compra()

    # Preencher dados e confirmar
    checkout = CheckoutPage(driver)
    checkout.preencher_dados("Joao", "Silva", "64000000")
    checkout.confirmar_pedido()

    # Validar sucesso
    mensagem = checkout.obter_mensagem_sucesso()
    assert mensagem == "Thank you for your order!"