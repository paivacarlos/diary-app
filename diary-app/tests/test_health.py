import pytest
import requests

BASE_URL = 'http://127.0.0.1:8000'

def test_health_check_status():
    response = requests.get(f'{BASE_URL}/health')
    response.status_code
    assert response.status_code == 200

def test_helth_check_message():
    response = requests.get(f'{BASE_URL}/health')
    response_dict = response.json()
    response_message = 'We are online! :)'
    assert response_dict['message'] == response_message