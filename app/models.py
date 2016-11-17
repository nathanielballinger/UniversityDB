#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_searchable import make_searchable, search
from sqlalchemy_utils.types import TSVectorType
import requests
import json
import urllib.request
import re

Base = declarative_base()
app = Flask(__name__)

make_searchable()

#Nate's Database

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bathory94@localhost:5432/swe'
#Chris's database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe2'
#Digital Ocean
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gusman772:MrSayanCanSing2@localhost:5432/swe2'

#Abhi's DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swe:asdfzxc@localhost:9000/swe'

db = SQLAlchemy(app)	
#db.configure_mappers()
manager = Manager(app)

def model_to_dict(obj):
	fields = {}
	for field in [entry for entry in dir(obj) if not entry.startswith('_') and entry != 'metadata']:
		data = obj.__getattribute__(field)
		try:
			json.dumps(data)
			fields[field] = data
		except TypeError:
			pass
	return fields

class Game(db.Model):
	__tablename__ = 'games'
	#Column values are name, release date, genre, developers/publisher, rating of first release
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, default = None)
	release_date = db.Column(db.String, default = None)
	#Page values are description, review, image, platforms, characters, aliases, site detail url
	description = db.Column(db.String, default = None)
	tiny_image = db.Column(db.String, default = None)
	medium_image = db.Column(db.String, default = None)
	#Define relationship with platforms. Links to table. Backref creates new property of platforms that list all games
	platforms = db.Column(db.String, default = None)
	character = db.Column(db.String, default = None)
	aliases = db.Column(db.String, default = None)
	site_detail_url = db.Column(db.String, default = None)
	search_vector = db.Column(TSVectorType('name'))

	def __init__(self,id,name,release_date,description,tiny_image,medium_image,platforms,aliases,site_detail_url):
		self.id = id
		self.name = name
		self.release_date = release_date
		self.description = description
		self.tiny_image = tiny_image
		self.medium_image = medium_image
		self.platforms = platforms
		self.aliases = aliases
		self.site_detail_url = site_detail_url

	def serialize(self):
		result = model_to_dict(self)
		parsedPlatforms = []
		parsedCharacters = []
		if result["platforms"] is not None:
			parsedPlatforms = result["platforms"].split("[[[[")
			parsedPlatforms = parsedPlatforms[:-1]
			for i in range (len(parsedPlatforms)):
				parsedPlatforms[i] = parsedPlatforms[i].split("||||")
				parsedPlatforms[i][0] = int(parsedPlatforms[i][0])

			result["platforms"] = parsedPlatforms
		if result["character"] is not None:
			parsedCharacters = result["character"].split("[[[[")
			parsedCharacters = parsedCharacters[:-1]
			for i in range (len(parsedCharacters)):
				parsedCharacters[i] = parsedCharacters[i].split("||||")
				parsedCharacters[i][0] = int(parsedCharacters[i][0])
			result["character"] = parsedCharacters
		#print(result)
		return result

	def serialize_table(self):
		platLength = 0
		if self.platforms is not None:
			platforms = self.platforms.split("[[[[")
			platLength = len(platforms)
		else:
			platLength = 0
		fields = {"id": self.id,"name": self.name, "release_date": self.release_date, "aliases": self.aliases, "tiny_image": self.tiny_image, "num platforms": platLength}
		return fields

class Platform(db.Model):
	__tablename__ = 'platforms'
	#Column values are name, release date, company, starting price, number of sold units
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, default = None)
	release_date = db.Column(db.String, default = None)
	company = db.Column(db.String, default = None)
	starting_price = db.Column(db.String, default = None)
	install_base = db.Column(db.String, default = None)
	#Page values are description, online support flag, abbreviations, site_detail_url, Image
	description = db.Column(db.String, default = None)
	online_support = db.Column(db.Boolean, default = None)
	abbreviations = db.Column(db.String, default = None)
	site_detail_url = db.Column(db.String, default = None)
	tiny_image = db.Column(db.String, default = None)
	medium_image = db.Column(db.String, default = None)
	games = db.Column(db.String, default = None)
	search_vector = db.Column(TSVectorType('name'))

	def __init__(self,id,name,release_date,company,starting_price,install_base, description,online_support,abbreviations,site_detail_url,tiny_image,medium_image):
		self.id = id
		self.name = name
		self.release_date = release_date
		self.company = company
		self.starting_price = starting_price
		self.install_base = install_base
		self.description = description
		self.online_support = online_support
		self.abbreviations = abbreviations
		self.site_detail_url = site_detail_url
		self.tiny_image = tiny_image
		self.medium_image = medium_image

	def serialize(self):
		result = model_to_dict(self)
		if result["games"] is not None:
			#print(result["games"])
			parsedGames = result["games"].split("[[[[")
			parsedGames = parsedGames[:-1]
			#print(parsedGames)
			for i in range (len(parsedGames)):
				parsedGames[i] = parsedGames[i].split("||||")
				#print(parsedGames[i])
				parsedGames[i][0] = int(parsedGames[i][0])
			result["games"] = parsedGames
		return result

	def serialize_table(self):
		return {"id": self.id, "name": self.name, "release_date": self.release_date, "company": self.company, "starting_price": self.starting_price, "tiny_image": self.tiny_image}

class Character(db.Model):
	__tablename__ = 'characters'
	#Column values are name, birthday, gender, deck, game first appeared in
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, default = None)
	birthday = db.Column(db.String, default = None)
	gender = db.Column(db.Integer, default = None)
	deck = db.Column(db.String, default = None)
	#Page Values are Description, Image, Site_Detail_URL, aliases
	description = db.Column(db.String, default = None)
	tiny_image = db.Column(db.String, default = None)
	medium_image = db.Column(db.String, default = None)
	site_detail_url = db.Column(db.String, default = None)
	aliases = db.Column(db.String, default = None)
	first_appeared_in_game = db.Column(db.String, default = None)
	search_vector = db.Column(TSVectorType('name'))

	def __init__(self,id,name,birthday,gender,deck, description, tiny_image, medium_image, site_detail_url, aliases, first_appeared_in_game):
		self.id = id
		self.name = name
		self.birthday = birthday
		self.gender = gender
		self.deck = deck
		self.description = description
		self.tiny_image = tiny_image
		self.medium_image = medium_image
		self.site_detail_url = site_detail_url
		self.aliases = aliases
		self.first_appeared_in_game = first_appeared_in_game

	def serialize(self):
		result = model_to_dict(self)
		parsedGame = result['first_appeared_in_game']
		if parsedGame is not None:
			ret_list = parsedGame.split("||||")
			ret_list[0] = int(ret_list[0])
		else:
			ret_list = None
		result['first_appeared_in_game'] = ret_list
		return result


	def serialize_table(self):
		if self.first_appeared_in_game is not None:
			ret_list = self.first_appeared_in_game.split('||||')
			ret_list[0] = int(ret_list[0])
		else:
			ret_list = None
		fields = {"id": self.id, "gender": self.gender, "name": self.name, "aliases": self.aliases, "first_appeared_in_game": ret_list, "deck": self.deck, "tiny_image": self.tiny_image, "birthday": self.birthday}
		return fields


class SearchResult:

	def __init__(self, id, name, pillar, searchText):
		self.id = id
		self.name = name
		self.pillar = pillar

		# Do something with searchText to create self.word_hits
		self.word_hits = []

		#ignore non-alpha characters, perserving whitespace
		filteredSearchText = re.sub(r"[^A-Za-z\s]+", '', searchText).split()
		nameWords = self.name.lower()
		for word in filteredSearchText:
			if word.lower() in nameWords:
				self.word_hits.append(word)
		

	def toJSON(self):
		return model_to_dict(self)


