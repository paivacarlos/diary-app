import requests
import json

BASE_URL = 'http://127.0.0.1:8000'

data = {
    "title": "Quinta da Regalera e Palacio de Monssarate",
    "city": "Sintre",
    "transport_ticket_total_value": 30.00,
    "hotel_total_value": 80.00,
    "remember": "A Regalera é sensacional com seus tuneis e palacio assim como o jardim de Monssaret e seu Palacio no estilo do romantismo"
}

def test_list_all_facts_should_be_status_200():
    pre_request_to_insert_facts_in_the_database = requests.post(f'{BASE_URL}/create-fact',
                             data=json.dumps(data),
                             headers={'Content-Type': 'application/json'})
    assert pre_request_to_insert_facts_in_the_database.status_code == 200

    response = requests.get(f'{BASE_URL}/list-all-facts')
    assert response.status_code == 200