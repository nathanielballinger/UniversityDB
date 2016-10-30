from flask import Flask, send_file, url_for, jsonify, request
from models import Game, Platform, Character
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import requests
import json
import urllib.request 
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)
manager = Manager(app)

Base = declarative_base()

db.drop_all()
db.create_all()
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
	time.sleep(1)

for platform in platforms:
	s = requests.get(platform, headers = headers)
	time.sleep(1)

for character in characters:
	t = requests.get(character, headers = headers)
	time.sleep(1)
"""

v = requests.get(characters[0], headers = headers)
data = v.json()
for entry in data['results']:
	c = Character(name = entry['name'], birthday = entry['birthday'], gender = entry['gender'], deck = entry['deck'], description = entry['description'], image = entry['image'], site_detail_url = entry['site_detail_url'], aliases = entry['aliases'])
	db.session.add(c)
	db.session.commit()
	print("Are we here")

print ("fuck you")
#Now we need to loop through every element in the json and add them to db

