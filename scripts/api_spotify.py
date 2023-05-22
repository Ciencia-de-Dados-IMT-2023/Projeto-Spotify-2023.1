import os
import pprint

import requests
from dotenv import load_dotenv


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


def make_req(route: str, id: str) -> requests.models.Response:
    url = f'https://api.spotify.com/v1/{route}/{id}'

    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    return response


def get_artist_data(artist_link: str) -> requests.models.Response:

    return make_req('artists', artist_link)


def get_track(id_track: str) -> requests.models.Response:

    return make_req('tracks', id_track)


def get_audio_features(id_musica: str) -> requests.models.Response:

    return make_req('audio-features', id_musica)


def get_playlist(id_playlist: str) -> requests.models.Response:

    return make_req('playlists', id_playlist)


def get_album(id_album: str) -> requests.models.Response:

    return make_req('albums', id_album)


def main():
    
    # 0. Pega o token da API
    # token = get_api_token()
    # print(token)


    # Pega os dados de música
    id_musica = '45Egmo7icyopuzJN0oMEdk?si=51fe34b203e24654'

    track = get_track(id_musica)
    print(track.json())


    # 1. Pega os dados do Hungria Hip Hop
    # artist_link = '0vLuOi2k62sHujIfplInlK?si=9ru2dX1nTRuRg_iLOjh1JA'

    # hungria_req = get_artist_data(artist_link)
    # print(hungria_req.json())
    

    # 2. Pega os dados de uma música - Crawling, Linkin Park
    # id_musica = '57BrRMwf9LrcmuOsyGilwr?si=bcfb65883f374f6c'

    # musica_req = get_audio_features(id_musica)
    # pprint.pprint(musica_req.json())


    # 3. Pegar os dados de uma playlist, Ficar Tranquilo
    # id_playlist = '2fLIJ2ABXxFLGUjvF34nAQ?si=43bb1b43430b4e82'

    # playlist_req = get_playlist(id_playlist)
    # # print(playlist_req.json())

    # # 3.1 Pega os dados de uma música da playlist
    # musica_playlist = playlist_req.json()['tracks']['items'][0]

    # # 3.1.1 Pega o nome da música
    # nome_musica = musica_playlist['track']['name']
    # print(nome_musica)

    # # 3.1.2 Pega o id da música
    # id_musica = musica_playlist['track']['id']

    # # 3.2 Pega os dados de uma música da playlist
    # musica_playlist_features = get_audio_features(id_musica)
    # print(musica_playlist_features.json())

    # 4. Pegar dados de um album
    # id_album = '3Q9wXhEAX7NYCPP0hxIuDz?si=jg6tLF24QSqCZ4xxWwT9-A'

    # album_req = get_album(id_album)
    # print(album_req.json().keys())

    # popularidade_album = album_req.json()['popularity']
    # print(popularidade_album)


if __name__ == '__main__':
    os.system('cls')

    load_dotenv()
    API_TOKEN = str(os.getenv('API_TOKEN'))

    main()
