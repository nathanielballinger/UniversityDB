#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)
manager = Manager(app)

Base = declarative_base()
#Many to many relationship table between characters and games
char_game = db.Table(db.Column('char_id',db.String, db.ForeignKey('characters.id')),db.Column('game_id',db.String,db.ForeignKey('games.id')))

#Many to many relationship table between games and platforms
plat_game = db.Table(db.Column('character_id', db.String, db.ForeignKey('characters.id')),db.Column('platform_id',db.String,db.ForeignKey('platforms.id')))

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