from fastapi.testclient import TestClient

from project.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/actuator/health-check")
    assert response.status_code == 200
    assert response.json() == "OK"

