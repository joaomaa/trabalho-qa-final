import requests

BASE_URL = "https://petstore.swagger.io/v2"

USERNAME = "joao_teste"

def test_criar_usuario():
    payload = {
        "id": 1,
        "username": USERNAME,
        "firstName": "Joao",
        "lastName": "Silva",
        "email": "joao@teste.com",
        "password": "senha123"
    }
    response = requests.post(f"{BASE_URL}/user", json=payload)

    assert response.status_code == 200

def test_buscar_usuario():
    response = requests.get(f"{BASE_URL}/user/{USERNAME}")

    assert response.status_code == 200
    assert response.json()["username"] == USERNAME

def test_atualizar_usuario():
    payload = {
        "id": 1,
        "username": USERNAME,
        "firstName": "Joao Atualizado",
        "lastName": "Silva",
        "email": "joao@teste.com",
        "password": "senha123"
    }
    response = requests.put(f"{BASE_URL}/user/{USERNAME}", json=payload)

    assert response.status_code == 200

def test_deletar_usuario():
    response = requests.delete(f"{BASE_URL}/user/{USERNAME}")

    assert response.status_code == 200