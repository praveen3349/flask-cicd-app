# tests/test_app.py
import pytest
from app import app as flask_app # Import the Flask app instance

@pytest.fixture
def client():
    # Use Flask's test client to simulate requests
    with flask_app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the / route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask App!" in response.data
    assert b"running" in response.data

def test_status_route(client):
    """Test the /status route."""
    response = client.get('/status')
    assert response.status_code == 200
    assert b"OK" in response.data
    assert b"version" in response.data
