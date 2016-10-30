import json
import urllib.request
import requests
from models import Game, Platform, Character


api_key="d0d1072f35f6c08b0ce0d7249c1c1d94d500c913"
"""
gameFieldList = "&field_list=id,name,original_release_date,genres,developers,original_rating,description,review,image,platforms,characters,aliases,site_detail_url"
platformFieldList ="&field_list=id,name,abbreviation,company,deck,description,image,install_base,online_support,original_price,release_date,site_detail_url"
characterFieldList = "&field_list=id,aliases,birthday,deck,description,enemies,friends,first_appeared_in_game,games,gender,image,name,site_detail_url"
"""

games = []
for x in range(0,522):
	gameString = "http://www.giantbomb.com/api/games/?api_key="+api_key+"&format=json&offset"+str(x)+"00"
	games.append(gameString)

platforms = []
for x in range(0,2):
	platformString = "http://www.giantbomb.com/api/platforms/?api_key="+api_key+"&format=json&offset"+str(x)+"00"
	platforms.append(platformString)

characters = []
for x in range(0,332):
	characterString = "http://www.giantbomb.com/api/characters/?api_key="+api_key+"&format=json&offset"+str(x)+"00"
	characters.append(characterString)

#Gets json from API
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
"""
for game in games:
	r = requests.get(game,headers=headers)

for platform in platforms:
	s = requests.get(platform, headers = headers)

for character in characters:
	t = requests.get(character, headers = headers)
"""
q = requests.get(platforms[0],headers = headers)
print(q.json())
v = requests.get(characters[0], headers = headers)
#print(v.json())



