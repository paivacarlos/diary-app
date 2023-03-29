import pytest
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('../.env')

BASE_URL = os.environ.get('ENV_LOCAL')

pre_request_data_to_payload = {
    "title": "Quinta da Regalera e Palacio de Monssarate",
    "city": "Sintra",
    "transport_ticket_total_value": 30.00,
    "hotel_total_value": 80.00,
    "remember": "A Regalera eh sensacional com seus tuneis e palacio assim como o jardim de Monssaret e seu Palacio no estilo do romantismo"
}

main_request_data_to_payload = {
    "title": "Templo de Diana",
    "city": "Évora",
    "transport_ticket_total_value": 26.00,
    "hotel_total_value": 90.00,
    "remember": "O templo de Diana é a construção romana mais ocidental do antigo Império Romano"
}




def test_update_fact_status_code_should_be_200():
    pre_request_response_from_post = requests.post(f'{BASE_URL}/create-fact',
                             data=json.dumps(pre_request_data_to_payload ),
                             headers={'Content-Type': 'application/json'})

    print(f'Response from POST: {pre_request_response_from_post.status_code}')
    assert pre_request_response_from_post.status_code == 200

    value = pre_request_response_from_post.__dict__
    array_aux = []
    value_2 = array_aux.append(value.get("_content"))
    print(f'folling the id: {value}')
    print(f'folling the id: {value.get("_content")}')
    print(f'folling the id: {value.get("_content")["b"][0]}')
    #id_created_from_post = pre_request_response_from_post

    main_response_from_put = requests.put(f'{BASE_URL}/create-fact',
                             data=json.dumps(main_request_data_to_payload),
                             headers={'Content-Type': 'application/json'})

    print(f'Response from PUT: {main_response_from_put.status_code}')
    assert main_response_from_put.status_code == 200
