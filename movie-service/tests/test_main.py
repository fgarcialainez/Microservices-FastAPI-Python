""" This module holds a basic test suite for all the movie-service endpoints"""
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    # Insntantiate the API client (waiting for DB)
    with TestClient(app) as c:
        yield c


def test_create_movie(client):
    # Create the payload
    payload = {
        'name': 'TestName',
        'plot': 'TestPlot',
        'genres': ['Genre1', 'Genre2'],
        'casts_id': []
    }

    # Execute the request
    response = client.post("/api/v1/movies/", json=payload)

    # Check the response data
    assert response.status_code == 201
    assert response.json()['name'] == 'TestName'
    assert response.json()['plot'] == 'TestPlot'


def test_get_movies(client):
    # Create the payload
    payload = {
        'name': 'TestName',
        'plot': 'TestPlot',
        'genres': ['Genre1', 'Genre2'],
        'casts_id': []
    }

    # Execute the request
    response = client.post("/api/v1/movies/", json=payload)

    # Check the response data
    assert response.status_code == 201
    assert response.json()['name'] == 'TestName'
    assert response.json()['plot'] == 'TestPlot'

    # Fetch all the movies
    response = client.get("/api/v1/movies/")

    # Check the response data
    assert response.status_code == 200


def test_get_movie(client):
    # Create the payload
    payload = {
        'name': 'TestName',
        'plot': 'TestPlot',
        'genres': ['Genre1', 'Genre2'],
        'casts_id': []
    }

    # Execute the request
    response = client.post("/api/v1/movies/", json=payload)

    # Check the response data
    assert response.status_code == 201
    assert response.json()['name'] == 'TestName'
    assert response.json()['plot'] == 'TestPlot'

    # Get the movie identifier
    movie_id = response.json()['id']

    # Fetch the movie
    response = client.get(f'/api/v1/movies/{str(movie_id)}/')

    # Check the response data
    assert response.status_code == 200
    assert response.json()['id'] == movie_id
    assert response.json()['name'] == 'TestName'
    assert response.json()['plot'] == 'TestPlot'


def test_get_invalid_movie(client):
    # Fetch an invalid movie
    response = client.get(f'/api/v1/movies/{1000}/')

    # Check the response data
    assert response.status_code == 404


def test_delete_movie(client):
    # Create the payload
    payload = {
        'name': 'TestName',
        'plot': 'TestPlot',
        'genres': ['Genre1', 'Genre2'],
        'casts_id': []
    }

    # Execute the request
    response = client.post("/api/v1/movies/", json=payload)

    # Check the response data
    assert response.status_code == 201
    assert response.json()['name'] == 'TestName'
    assert response.json()['plot'] == 'TestPlot'

    # Get the movie identifier
    movie_id = response.json()['id']

    # Delete the movie
    response = client.delete(f'/api/v1/movies/{str(movie_id)}/')

    # Check the response data
    assert response.status_code == 204
