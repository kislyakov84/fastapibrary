from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"title": "New Book", "available_copies": 5})
    assert response.status_code == 200
    assert response.json()["title"] == "New Book"