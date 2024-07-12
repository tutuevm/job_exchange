from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    response = client.get('/get_status')
    assert response.status_code == 200
    assert response.json() == {'message': 'OK'}