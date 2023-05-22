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

    if response.status_code != 200:
        print(f'Erro: {response.status_code}')
        print(f'Erro: {response.json()}')
        import sys
        sys.exit(1)

    else:
        return response


def get_artist_data(id_artist: str) -> requests.models.Response:

    return make_req('artists', id_artist)


def get_track(id_track: str) -> requests.models.Response:

    return make_req('tracks', id_track)


def get_audio_features(id_track: str) -> requests.models.Response:

    return make_req('audio-features', id_track)


def get_playlist(id_playlist: str) -> requests.models.Response:

    return make_req('playlists', id_playlist)


def get_album(id_album: str) -> requests.models.Response:

    return make_req('albums', id_album)


def main():
    
    # 0. Get API Token
    # token = get_api_token()
    # print(token)


    # 1. Get music data
    print('1. Music data\n')
    id_musica = '1odExI7RdWc4BT515LTAwj?si=a72394989db84d65'

    track = get_track(id_musica)
    audio_features = get_audio_features(id_musica)

    # 1.1 Extracting some information
    music_name = track.json()['name']
    duration = track.json()['duration_ms']
    popularity = track.json()['popularity']
    release_date = track.json()['album']['release_date']
    danceability = audio_features.json()['danceability']
    energy = audio_features.json()['energy']
    speechiness = audio_features.json()['speechiness']

    print(f'Music name: {music_name}')
    print(f'Durating: {duration} ms')
    print(f'Popularity: {popularity}/100')
    print(f'Release Date: {release_date}')
    print(f'Danceability: {danceability}')
    print(f'Energy: {energy}')
    print(f'Speechiness: {speechiness}')

    
    # 2. Get artist data
    print()
    print('2. Artist data\n')
    id_artist = track.json()['artists'][0]['id']

    artist = get_artist_data(id_artist)

    # 2.1 Extracting some information
    artist_name = artist.json()['name']
    artist_popularity = artist.json()['popularity']
    artist_followers = artist.json()['followers']['total']
    artist_genres = artist.json()['genres']

    print(f'Artist Name: {artist_name}')
    print(f'Artist Popularity: {artist_popularity}/100')
    print(f'Artist Followers: {artist_followers}')
    print(f'Artist Genres: {artist_genres}')


    # 3. Get album data
    print()
    print('3. Album data\n')
    id_album = track.json()['album']['id']

    album = get_album(id_album)

    # 3.1 Extracting some information
    album_name = album.json()['name']
    album_type = album.json()['album_type']
    album_release_date = album.json()['release_date']
    album_total_tracks = album.json()['total_tracks']
    album_popularity = album.json()['popularity']

    print(f'Album Name: {album_name}')
    print(f'Album Type: {album_type}')
    print(f'Album Release Date: {album_release_date}')
    print(f'Album Total Tracks: {album_total_tracks}')
    print(f'Album Popularity: {album_popularity}/100')







    # 1. Pega os dados do Hungria Hip Hop
    # artist_link = '0vLuOi2k62sHujIfplInlK?si=9ru2dX1nTRuRg_iLOjh1JA'

    # hungria_req = get_artist_data(artist_link)
    # print(hungria_req.json())
    


    # 3. Pegar os dados de uma playlist, Ficar Tranquilo
    # id_playlist = '1gCZcgXAbPo85wAwSgy299?si=eee6417f6dcc445d'

    # playlist_req = get_playlist(id_playlist)
    # # print(playlist_req.json())

    # # 3.1 Pega os dados de uma música da playlist
    # import json
    # musica_playlist = playlist_req.json()['tracks']#['items'][0]
    # with open('a.json', 'w') as file:
    #     file.write(json.dumps(musica_playlist, indent=4))

    # 3.1.1 Pega o nome da música
    # nome_musica = musica_playlist['track']['name']
    # print(nome_musica)

    # # 3.1.2 Pega o id da música
    # id_musica = musica_playlist['track']['id']

    # # 3.2 Pega os dados de uma música da playlist
    # musica_playlist_features = get_audio_features(id_musica)
    # print(musica_playlist_features.json())

    # # 4. Pegar dados de um album
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
