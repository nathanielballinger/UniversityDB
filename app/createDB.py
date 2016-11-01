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
print("PASSED THE GAULTLET")
api_key="d0d1072f35f6c08b0ce0d7249c1c1d94d500c913"

gameFieldList = "&field_list=id,name,original_release_date,genres,developers,original_rating,description,review,image,platforms,characters,aliases,site_detail_url"
platformFieldList ="&field_list=id,name,abbreviation,company,deck,description,image,install_base,online_support,original_price,release_date,site_detail_url"
characterFieldList = "&field_list=id,aliases,birthday,deck,description,enemies,friends,first_appeared_in_game,games,gender,image,name,site_detail_url"


games = []
for x in range(0,520):
	gameString = "http://www.giantbomb.com/api/games/?api_key="+api_key+"&format=json&offset="+str(x)+"00"
	games.append(gameString)

platforms = []
for x in range(0,2):
	platformString = "http://www.giantbomb.com/api/platforms/?api_key="+api_key+"&format=json&offset="+str(x)+"00"
	platforms.append(platformString)

characters = []
for x in range(0,332):
	if x ==26:
		continue
	characterString = "http://www.giantbomb.com/api/characters/?api_key="+api_key+"&format=json&offset="+str(x)+"00"
	characters.append(characterString)

#Gets json from API
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
print("Adding to DB...this step will take approx 20 mins")
counter = 0
for game in games:
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
		db.session.add(g)
		db.session.commit()

	time.sleep(1)
	print(str(counter)+"/519 complete")
	counter+=1

print("LOADING GAMES COMPLETE")
nc = 0
for platform in platforms:
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
		p = Platform(id = entry['id'], name = entry['name'], release_date = entry['release_date'], company = company, starting_price = entry['original_price'], description = entry['description'], install_base = entry['install_base'], online_support = entry['online_support'], abbreviations = entry['abbreviation'], site_detail_url = entry['site_detail_url'], tiny_image = tiny_image, medium_image = medium_image)
		db.session.add(p)
		db.session.commit()
	time.sleep(1)
	print(str(counter)+"/2 complete")
	counter+=1

print("LOADING PLATFORMS COMPLETE")

dnc = 0
for character in characters:
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
		c = Character(id = entry['id'], name = entry['name'], birthday = entry['birthday'], gender = entry['gender'], deck = entry['deck'], description = entry['description'], tiny_image = tiny_image, medium_image = medium_image, site_detail_url = entry['site_detail_url'], aliases = entry['aliases'],first_appeared_in_game = first_appeared_in_game)
		db.session.add(c)
		db.session.commit()
	time.sleep(1)
	print(str(counter)+"331 complete")
	counter+=1
print("LOADING CHARACTERS COMPLETE...MAKING SOME FINAL MODIFCATIONS")

#List of games for each platform
plat_array = ['']*164
for i in range(1,56877):

	b = Game.query.filter_by(id = i).first()
	if b is None:
		continue
	if b.platforms is None:
		continue
	plat_list = b.platforms.split('.')
	plat_list = plat_list[:-1]
	for x in plat_list:
		plat_array[int(x)-1]+=str(i)
		plat_array[int(x)-1]+='.'

counter = 1
for entry in plat_array:
	if entry is not '':
		p = Platform.query.filter_by(id = counter).first()

		p.games = entry
		db.session.commit()
		counter +=1
	else:
		counter+=1

#List of characters for each game
chr_array = ['']*56877
for i in range(1,34113):

	b = Character.query.filter_by(id = i).first()
	if b is None:
		continue
	if b.first_appeared_in_game is None:
		continue
	the_game = b.first_appeared_in_game
	chr_array[int(the_game)] = i


counter = 1
for entry in chr_array:
	if entry is not '':
		p = Game.query.filter_by(id = counter).first()
		p.character = entry
		db.session.commit()
		counter +=1
	else:
		counter+=1

