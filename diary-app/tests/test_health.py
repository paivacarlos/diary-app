import pytest
import requests

BASE_URL = 'http://127.0.0.1:8000'

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    response.status_code
    assert response.status_code == 200