import os
from dotenv import load_dotenv

import requests


def get_api_token() -> str:
    url = 'https://accounts.spotify.com/api/token'

    payload = {
        'grant_type': 'client_credentials',
        'client_id': str(os.getenv('CLIENT_ID')),
        'client_secret': str(os.getenv('CLIENT_SECRET'))
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()['access_token']


def main():
    
    token = get_api_token()
    print(token)


if __name__ == '__main__':
    os.system('cls')

    load_dotenv()
    main()