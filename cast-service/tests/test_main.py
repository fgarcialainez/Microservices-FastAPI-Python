""" This module holds a basic test suite for all the cast service endpoints"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

# Insntantiate the API client
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_cast(client):
    # Create the payload
    payload = {
        'name': 'TestCast',
        'nationality': 'TestNationality'
    }

    # Execute the request
    response = client.post("/api/v1/casts/", json=payload)

    # Check the response data
    assert response.status_code == 201
    assert response.json()['name'] == 'TestCast'
    assert response.json()['nationality'] == 'TestNationality'


def test_get_cast(client):
    # Create the payload
    payload = {
        'name': 'TestCast',
        'nationality': 'TestNationality'
    }

    # Execute the request
    response = client.post("/api/v1/casts/", json=payload)

    # Check the response data
    assert response.status_code == 201
    assert response.json()['id']
    assert response.json()['name'] == 'TestCast'
    assert response.json()['nationality'] == 'TestNationality'

    # Get the cast identifier
    cast_id = response.json()['id']

    # Fetch the cast
    response = client.get("/api/v1/casts/" + str(cast_id))

    # Check the response data
    assert response.status_code == 200
    assert response.json()['id'] == cast_id
    assert response.json()['name'] == 'TestCast'
    assert response.json()['nationality'] == 'TestNationality'


def test_get_invalid_cast(client):
    # Fetch an invalid cast
    response = client.get("/api/v1/casts/" + str(1000))

    # Check the response data
    assert response.status_code == 404
