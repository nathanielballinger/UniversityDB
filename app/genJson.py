from flask import Flask, send_file, url_for, jsonify, request
from models import Game, Platform, Character
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import requests
import json
import urllib.request 
import time
from models import db

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
for x in range(8,520):
	gameString = "http://www.giantbomb.com/api/games/?api_key="+api_key+"&format=json&offset="+str(x)+"00"
	games.append(gameString)

platforms = []
for x in range(0,2):
	platformString = "http://www.giantbomb.com/api/platforms/?api_key="+api_key+"&format=json&offset="+str(x)+"00"
	platforms.append(platformString)

characters = []
for x in range(31,332):
	if x ==26:
		continue
	characterString = "http://www.giantbomb.com/api/characters/?api_key="+api_key+"&format=json&offset="+str(x)+"00"
	characters.append(characterString)

#Gets json from API
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

for game in games:
	print(game)
	v = requests.get(game,headers=headers)
	game_data = v.json()
	for entry in game_data['results']:
		image_dict = entry['image']
		if image_dict is None:
			tiny_image = None
			medium_image = None
		else:
			tiny_image = image_dict['tiny_url']
			medium_image = image_dict['medium_url']
		plat_string = ''
		plat_data = entry['platforms']
		if plat_data is not None:
			for plat in plat_data:
				plat_string += str(plat['id']) + '.'
		else:
			plat_string = None
		g = Game(id = entry['id'], name = entry['name'], release_date = entry['original_release_date'], description = entry['description'], tiny_image = tiny_image, medium_image = medium_image, platforms = plat_string, aliases = entry['aliases'], site_detail_url = entry['site_detail_url'])
		print(g.id)
		db.session.add(g)
		db.session.commit()
	time.sleep(1)
"""
for platform in platforms:
	print(platform)
	v = requests.get(platform, headers = headers)
	platform_data = v.json()
	for entry in platform_data['results']:
		image_dict = entry['image']
		if entry['company'] is None:
			company = None
		else:
			company = entry['company']['name']
		if image_dict is None:
			tiny_image = None
			medium_image = None
		else:
			tiny_image = image_dict['tiny_url']
			medium_image = image_dict['medium_url']
		p = Platform(id = entry['id'], name = entry['name'], release_date = entry['release_date'], company = company, starting_price = entry['original_price'], description = entry['description'], online_support = entry['online_support'], abbreviations = entry['abbreviation'], site_detail_url = entry['site_detail_url'], tiny_image = tiny_image, medium_image = medium_image)
		db.session.add(p)
		print(p.id)
		db.session.commit()
	time.sleep(1)

for character in characters:
	print (character)
	v = requests.get(character, headers = headers)
	character_data = v.json()
	for entry in character_data['results']:
		image_dict = entry['image']
		if entry['first_appeared_in_game'] is not None:
			first_appeared_in_game = entry['first_appeared_in_game']['id']
		else:
			first_appeared_in_game = None

		if image_dict is None:
			tiny_image = None
			medium_image = None
		else:
			tiny_image = image_dict['tiny_url']
			medium_image = image_dict['medium_url']
		print(entry['id'])
		c = Character(id = entry['id'], name = entry['name'], birthday = entry['birthday'], gender = entry['gender'], deck = entry['deck'], description = entry['description'], tiny_image = tiny_image, medium_image = medium_image, site_detail_url = entry['site_detail_url'], aliases = entry['aliases'],first_appeared_in_game = first_appeared_in_game)
		counter+=1
		db.session.add(c)
		db.session.commit()
	time.sleep(1)


v = requests.get(games[0], headers = headers)
game_data = v.json()
for entry in game_data['results']:
	image_dict = entry['image']
	if image_dict is None:
		tiny_image = None
		medium_image = None
	else:
		tiny_image = image_dict['tiny_url']
		medium_image = image_dict['medium_url']
	plat_string = ''
	plat_data = entry['platforms']
	for plat in plat_data:
		plat_string += str(plat['id']) + '.'
	g = Game(id = entry['id'], name = entry['name'], release_date = entry['original_release_date'], description = entry['description'], tiny_image = tiny_image, medium_image = medium_image, platforms = plat_string, aliases = entry['aliases'], site_detail_url = entry['site_detail_url'])
	print(plat_string)
	print(g.id)
	db.session.add(g)
	db.session.commit()




"""
#Now we need to loop through every element in the json and add them to db

