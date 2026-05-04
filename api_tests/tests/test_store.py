import requests

BASE_URL = "https://petstore.swagger.io/v2"

ORDER_ID = 1

def test_buscar_inventario():
    response = requests.get(f"{BASE_URL}/store/inventory")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_criar_pedido():
    payload = {
        "id": ORDER_ID,
        "petId": 123456,
        "quantity": 1,
        "status": "placed"
    }
    response = requests.post(f"{BASE_URL}/store/order", json=payload)

    assert response.status_code == 200
    assert response.json()["id"] == ORDER_ID
    assert response.json()["status"] == "placed"

def test_buscar_pedido():
    response = requests.get(f"{BASE_URL}/store/order/{ORDER_ID}")

    assert response.status_code == 200
    assert response.json()["id"] == ORDER_ID

def test_deletar_pedido():
    response = requests.delete(f"{BASE_URL}/store/order/{ORDER_ID}")

    assert response.status_code == 200