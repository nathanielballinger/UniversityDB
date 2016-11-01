#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import requests
import json
import urllib.request 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe1'

db = SQLAlchemy(app)
manager = Manager(app)

Base = declarative_base()

db.create_all()

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
	aliases = db.Column(db.String)
	site_detail_url = db.Column(db.String)

	def __repr__(self):
		return '<Game %r>' % self.name

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
	def __repr__(self):
		return '<Platform %r>' % self.name


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
	
	def __repr__(self):
		return '<Character %r>' % self.name


if __name__ == "__main__":
    manager.run()       # Update this line to use the manager
