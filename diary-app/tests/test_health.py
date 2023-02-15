import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv('../.env')

BASE_URL = os.environ.get('ENV_LOCAL')


def test_health_check_status():
    response = requests.get(f'{BASE_URL}/health')
    response.status_code
    assert response.status_code == 200


def test_health_check_message():
    response = requests.get(f'{BASE_URL}/health')
    response_dict = response.json()
    response_message = 'We are online! :)'
    assert response_dict['message'] == response_message
