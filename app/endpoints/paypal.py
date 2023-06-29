import requests

BASE_URL = 'https://api-m.sandbox.paypal.com'
CLIENT_ID = ''
SECRET = ''

def create_payment(amount, currency):
    url = BASE_URL + '/v1/payments/payment'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = {
        'intent': 'sale',
        'payer': {
            'payment_method': 'paypal'
        },
        'transactions': [
            {
                'amount': {
                    'total': str(amount),
                    'currency': currency
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def execute_payment(payment_id, payer_id):
    url = BASE_URL + f'/v1/payments/payment/{payment_id}/execute'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = {
        'payer_id': payer_id
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_access_token():
    url = BASE_URL + '/v1/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {get_auth_token()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    return response_json['access_token']


def get_auth_token():
    return f'{CLIENT_ID}:{SECRET}'.encode('utf-8').b64encode()