#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import requests
import json
import urllib.request 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)
manager = Manager(app)

Base = declarative_base()
#Many to many relationship table between characters and games
char_game = db.Table(db.Column('char_id',db.String, db.ForeignKey('characters.id')),db.Column('game_id',db.String,db.ForeignKey('games.id')))

#Many to many relationship table between games and platforms
plat_game = db.Table(db.Column('character_id', db.String, db.ForeignKey('characters.id')),db.Column('platform_id',db.String,db.ForeignKey('platforms.id')))

#Many to many relationship table between platforms and characters
plat_char = db.Table(db.Column('platform_id', db.String, db.ForeignKey('platforms.id')),db.Column('character_id',db.String,db.ForeignKey('characters.id')))

class Game(db.Model):
	__tablename__ = 'games'
	#Column values are name, release date, genre, developers/publisher, rating of first release
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	release_date = db.Column(db.String)
	genre = db.Column(db.String)
	developers = db.Column(db.String)
	rating = db.Column(db.String)
	#Page values are description, review, image, platforms, characters, aliases, site detail url
	description = db.Column(db.String)
	review = db.Column(db.String)
	image = db.Column(db.String)
	#Define relationship with platforms. Links to table. Backref creates new property of platforms that list all games
	platforms = db.relationship('Platform', secondary = plat_game, backref = db.backref('games'))
	characters = db.relationship('Character', secondary = char_game, backref = db.backref('games'))

	aliases = db.Column(db.String)
	site_detail_url = db.Column(db.String)

	def __init__(self,id,name,release_date,genre,developers,rating,description,review,image,platforms,characters):
		self.id = id
		self.name = name
		self.release_date = release_date
		self.genre = genre
		self.developers = developers
		self.rating = rating
		self.description = description
		self.review = review
		self.image = image
		self.platforms = platforms
		self.characters = characters

	def __repr__(self):
		return '<Game %r>' % self.name

class Platform(db.Model):
	__tablename__ = 'platforms'
	#Column values are name, release date, company, starting price, number of sold units
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	release_date = db.Column(db.String)
	company = db.Column(db.String)
	starting_price = db.Column(db.String)
	number_units_sold = db.Column(db.String)
	#Page values are description, online support flag, abbreviations, site_detail_url, Image
	description = db.Column(db.String)
	online_support = db.Column(db.String)
	abbreviations = db.Column(db.String)
	site_detail_url = db.Column(db.String)
	image = db.Column(db.String)

	games = db.relationship('Game', secondary = plat_game, backref = db.backref('platforms'))
	characters = db.relationship('Character', secondary = plat_char, backref = db.backref('platforms'))

	def __init__(self,id,name,release_date,company,starting_price,number_units_sold,description,online_support,abbreviations,site_detail_url,image):
		self.id = id
		self.name = name
		self.release_date = release_date
		self.company = company
		self.starting_price = starting_price
		self.number_units_sold = number_units_sold
		self.description = description
		self.online_support = online_support
		self.abbreviations = abbreviations
		self.site_detail_url = site_detail_url
		self.image = image

	def __repr__(self):
		return '<Platform %r>' % self.name


class Character(db.Model):
	__tablename__ = 'characters'
	#Column values are name, birthday, gender, deck, game first appeared in
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	birthday = db.Column(db.String)
	gender = db.Column(db.String)
	deck = db.Column(db.String)
	game_first_appeared = db.relationship('Game', backref = 'person')
	#Page Values are Description, Image, Site_Detail_URL, aliases
	description = db.Column(db.String)
	image = db.Column(db.String)
	site_detail_url = db.Column(db.String)
	aliases = db.Column(db.String)

	def __init__(self,id,name,birthday,gender,deck,game_first_appeared, description, image, site_detail_url, aliases):
		self.id = id
		self.name = name
		self.gender = gender
		self.deck
		self.game_first_appeared
		self.description = description
		self.image = image
		self.site_detail_url = site_detail_url
		self.aliases = aliases

	def __repr__(self):
		return '<Character %r> % self.name'


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
