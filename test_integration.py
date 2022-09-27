
from app.main import app
from fastapi.testclient import TestClient


def test_add_article():
    response = app.post('/articles/add')
    assert response.status_code == 200