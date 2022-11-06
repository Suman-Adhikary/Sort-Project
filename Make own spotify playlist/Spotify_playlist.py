from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ')

response = requests.get('https://www.billboard.com/charts/hot-100/' + Date)
bill_web = response.text

soup = BeautifulSoup(bill_web, 'html.parser')

song_names = [song.getText().strip() for song in soup.select(selector='li h3', class_='c-title')]
top_100 = song_names[0:100]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id='Your id',
        client_secret='Your secret',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = Date.split('-')[0]
for song in top_100:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except:
        print(f"{song} doesn't exist in Spotify. Skipped.")  

playlist = sp.user_playlist_create(user=user_id, name=f"{Date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)          