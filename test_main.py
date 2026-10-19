from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    assert client.get("/").status_code == 200

def test_health():
    assert client.get("/health").json() == {"status": "ok"}