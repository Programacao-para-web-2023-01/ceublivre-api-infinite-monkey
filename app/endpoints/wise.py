import requests

BASE_URL = 'https://api.sandbox.transferwise.tech/v3' 
API_TOKEN = 'your_api_token'


def create_transfer(source_currency, target_currency, amount):
    url = BASE_URL + '/transfers'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'source': source_currency,
        'target': target_currency,
        'amount': amount
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_transfer(transfer_id):
    url = BASE_URL + f'/transfers/{transfer_id}'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)
    return response.json()


def cancel_transfer(transfer_id):
    url = BASE_URL + f'/transfers/{transfer_id}/cancel'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.post(url, headers=headers)
    return response.json()
