import pytest
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('../.env')

BASE_URL = os.environ.get('ENV_LOCAL')

data = {
    "title": "Quinta da Regalera e Palacio de Monssarate",
    "city": "Sintre",
    "transport_ticket_total_value": 30.00,
    "hotel_total_value": 80.00,
    "remember": "A Regalera é sensacional com seus tuneis e palacio assim como o jardim de Monssaret e seu Palacio no estilo do romantismo"
}


def test_create_fact_status_code_should_be_200():
    response = requests.post(f'{BASE_URL}/create-fact',
                             data=json.dumps(data),
                             headers={'Content-Type': 'application/json'})

    assert response.status_code == 200
