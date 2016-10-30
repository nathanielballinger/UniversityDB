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
#char_game = db.Table(db.Column('char_id',db.String, db.ForeignKey('characters.id')),db.Column('game_id',db.String,db.ForeignKey('games.id')))

#Many to many relationship table between games and platforms
#plat_game = db.Table(db.Column('character_id', db.String, db.ForeignKey('characters.id')),db.Column('platform_id',db.String,db.ForeignKey('platforms.id')))

#Many to many relationship table between platforms and characters
#plat_char = db.Table(db.Column('platform_id', db.String, db.ForeignKey('platforms.id')),db.Column('character_id',db.String,db.ForeignKey('characters.id')))

class Game(db.Model):
	__tablename__ = 'games'
	#Column values are name, release date, genre, developers/publisher, rating of first release
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, default = None)
	release_date = db.Column(db.String, default = None)
	genre = db.Column(db.String, default = None)
	developers = db.Column(db.String, default = None)
	rating = db.Column(db.String, default = None)
	#Page values are description, review, image, platforms, characters, aliases, site detail url
	description = db.Column(db.String, default = None)
	review = db.Column(db.String, default = None)
	image = db.Column(db.String, default = None)
	#Define relationship with platforms. Links to table. Backref creates new property of platforms that list all games
	#platforms = db.relationship('Platform', secondary = plat_game, backref = db.backref('games'))
	#characters = db.relationship('Character', secondary = char_game, backref = db.backref('games'))

	aliases = db.Column(db.String)
	site_detail_url = db.Column(db.String)
	"""
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
	"""
	def __repr__(self):
		return '<Game %r>' % self.name

class Platform(db.Model):
	__tablename__ = 'platforms'
	#Column values are name, release date, company, starting price, number of sold units
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, default = None)
	release_date = db.Column(db.String, default = None)
	company = db.Column(db.String, default = None)
	starting_price = db.Column(db.String, default = None)
	number_units_sold = db.Column(db.String, default = None)
	#Page values are description, online support flag, abbreviations, site_detail_url, Image
	description = db.Column(db.String, default = None)
	online_support = db.Column(db.String, default = None)
	abbreviations = db.Column(db.String, default = None)
	site_detail_url = db.Column(db.String, default = None)
	image = db.Column(db.String, default = None)

	#games = db.relationship('Game', secondary = plat_game, backref = db.backref('platforms'))
	#characters = db.relationship('Character', secondary = plat_char, backref = db.backref('platforms'))
	"""
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
	"""
	def __repr__(self):
		return '<Platform %r>' % self.name


class Character(db.Model):
	__tablename__ = 'characters'
	#Column values are name, birthday, gender, deck, game first appeared in
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, default = None)
	birthday = db.Column(db.String, default = None)
	gender = db.Column(db.String, default = None)
	deck = db.Column(db.String, default = None)
	#first_appeared_in_game = db.relationship('Game', backref = 'person')
	#Page Values are Description, Image, Site_Detail_URL, aliases
	description = db.Column(db.String, default = None)
	image = db.Column(db.String, default = None)
	site_detail_url = db.Column(db.String, default = None)
	aliases = db.Column(db.String, default = None)
	"""
	#Add first appeared in game back to init
	def __init__(self,id,name,birthday,gender,deck, description, image, site_detail_url, aliases):
		self.id = id
		self.name = name
		self.birthday = birthday
		self.gender = gender
		self.deck = deck
		#self.first_appeared_in_game = first_appeared_in_game
		self.description = description
		self.image = image
		self.site_detail_url = site_detail_url
		self.aliases = aliases
	"""
	def __repr__(self):
		return '<Character %r>' % self.name


