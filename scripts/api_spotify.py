import os

import requests
from dotenv import load_dotenv


def get_api_token() -> requests.models.Response:
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


def get_artist_data(artist_link: str) -> requests.models.Response:

    url = f'https://api.spotify.com/v1/artists/{artist_link}'

    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    return response


def get_audio_features(id_musica: str) -> requests.models.Response:

    url = f'https://api.spotify.com/v1/audio-features/{id_musica}'

    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    return response


def get_playlist(id_playlist: str) -> requests.models.Response:

    url = f'https://api.spotify.com/v1/playlists/{id_playlist}'

    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    return response


def main():
    
    # 0. Pega o token da API
    # token = get_api_token()
    # print(token)


    # 1. Pega os dados do Hungria Hip Hop
    # artist_link = '0vLuOi2k62sHujIfplInlK?si=9ru2dX1nTRuRg_iLOjh1JA'

    # hungria_req = get_artist_data(artist_link)
    # print(hungria_req.json())
    

    # 2. Pega os dados de uma música - Crawling, Linkin Park
    # id_musica = '57BrRMwf9LrcmuOsyGilwr?si=bcfb65883f374f6c'

    # musica_req = get_audio_features(id_musica)
    # print(musica_req.json())


    # 3. Pegar os dados de uma playlist, Fica Tranquilo
    id_playlist = '2fLIJ2ABXxFLGUjvF34nAQ?si=43bb1b43430b4e82'

    playlist_req = get_playlist(id_playlist)
    # print(playlist_req.json())

    # 3.1 Pega os dados de uma música da playlist
    musica_playlist = playlist_req.json()['tracks']['items'][0]

    # 3.1.1 Pega o nome da música
    nome_musica = musica_playlist['track']['name']
    print(nome_musica)

    # 3.1.2 Pega o id da música
    id_musica = musica_playlist['track']['id']

    # 3.2 Pega os dados de uma música da playlist
    musica_playlist_features = get_audio_features(id_musica)
    print(musica_playlist_features.json())   


if __name__ == '__main__':

    load_dotenv()
    API_TOKEN = str(os.getenv('API_TOKEN'))

    main()
