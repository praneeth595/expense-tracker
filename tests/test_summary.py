from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_summary():
    response = client.get("/api/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "per_category" in data

