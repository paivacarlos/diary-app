import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('../.env')

BASE_URL = os.environ.get('ENV_LOCAL')


def test_list_all_facts_should_be_status_200():
    response = requests.get(f'{BASE_URL}/list-all-facts')
    assert response.status_code == 200
