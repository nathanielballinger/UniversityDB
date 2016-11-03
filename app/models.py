#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import requests
import json
import urllib.request
import re

Base = declarative_base()
app = Flask(__name__)
#Chris's database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe2'
#Digital Ocean
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gusman772:MrSayanCanSing2@localhost:5432/swe'
#Abhi's DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swe:asdfzxc@localhost:9000/swe'

db = SQLAlchemy(app)	
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
	
	def __repr__(self):
		return '<Game %r>' % self.name

	def serialize(self):
		result = model_to_dict(self)
		parsedPlatforms = []
		parsedCharacters = []
		if result["platforms"] is not None:
			parsedPlatforms = re.split(r"\.", result["platforms"])
			parsedPlatforms = parsedPlatforms[:-1]
			for i in range (len(parsedPlatforms)):
				parsedPlatforms[i] = int(parsedPlatforms[i])
			result["platforms"] = parsedPlatforms
		if result["character"] is not None:
			parsedCharacters = re.split(r"\.", result["character"])
			parsedCharacters = parsedCharacters[:-1]
			for i in range (len(parsedCharacters)):
				parsedCharacters[i] = int(parsedCharacters[i])
			result["platforms"] = parsedPlatforms
			result["character"] = parsedCharacters
		print(result)
		return result

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

	def __repr__(self):
		return '<Platform %r>' % self.name

	def serialize(self):
		result = model_to_dict(self)
		parsedGames = re.split(r"\.", result["games"])
		if result["games"] is not None:
			parsedGames = re.split(r"\.", result["games"])
			parsedGames = parsedGames[:-1]
			for i in range (len(parsedGames)):
				parsedGames[i] = int(parsedGames[i])
			result["games"] = parsedGames
		return result

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
	first_appeared_in_game = db.Column(db.Integer, default = None)

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
	
	def __repr__(self):
		return '<Character %r>' % self.name

	def serialize(self):
		return model_to_dict(self)

