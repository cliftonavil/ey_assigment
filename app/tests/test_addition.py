import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)


def test_addition():
    request_data = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/add", json=request_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["batchid"] == "id0101"
    assert response_data["response"] == [3, 7]
    assert response_data["status"] == "complete"
    assert "started_at" in response_data
    assert "completed_at" in response_data


def test_addition_empty_payload():
    request_data = {
        "batchid": "id0102",
        "payload": []
    }
    response = client.post("/add", json=request_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["batchid"] == "id0102"
    assert response_data["response"] == []
    assert response_data["status"] == "complete"
    assert "started_at" in response_data
    assert "completed_at" in response_data


def test_addition_invalid_payload():
    request_data = {
        "batchid": "id0103",
        "payload": [[1, "a"], [3, 4]]
    }
    response = client.post("/add", json=request_data)
    assert response.status_code == 422
