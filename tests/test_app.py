from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Message': 'Hello World'}
