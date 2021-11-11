from fastapi.testclient import TestClient
import main
import requests
import pytest


@pytest.fixture(scope="module")
def client():
    with TestClient(main.app) as client:
        yield client


def test_send_email(client: TestClient):
    response = client.post('/email/send')
    assert response.status_code == 200
