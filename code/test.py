from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola CI/CD"}

def test_sum():
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5