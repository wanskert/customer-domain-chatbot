from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_classify_endpoint():
    r = client.post("/classify", json={"text": "I want a refund"})
    assert r.status_code == 200
    assert "intent" in r.json()
