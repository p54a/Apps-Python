import requests
import json

resp = requests.get("https://id.twitch.tv/oauth2/token?client_id=abcdefg12345&client_secret=hijklmn67890&grant_type=client_credentials")
print (resp.json())