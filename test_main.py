from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def run_classification():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
