import pytest

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL