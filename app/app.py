#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_searchable import search
import json
import time
import re
import requests
import urllib.request
from tests import runTestsOut

#Only add app. on the next two lines when you want to run the DO server
import models
from models import Game, Character, Platform, db, Base, app, manager, SearchResult

#Chris's DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe2'
#Digital Ocean DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gusman772:MrSayanCanSing2@localhost:5432/swe2'
#Abhi's DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swe:asdfzxc@localhost:9000/swe2'


for i in range (0,50):
	p = Character.query.filter_by(id = i).first()
	if p is None:
		continue
	print(p.name)
	print(p.first_appeared_in_game)

@app.route("/")
def index():
	return send_file("templates/index.html")

# api interface
@app.route('/api/')
def api_root():
	data = {
		'urls': {
			'games_url': '/games',
			'characters_url': '/characters',
			'platforms_url': '/platforms'
		}
	}
	return jsonify(data)

@app.route('/researchpapers/<year>')
def research_papers_year(year):
	v = requests.get('http://researchpapers.me/api/year/' + str(year))
	#v = requests.get('http://127.0.0.1:5000/api/games/offset/1')
	print("DJDJFJDJDJJS")
	my_dict = v.json()
	ret_val = my_dict['years']
	return jsonify(ret_val)

@app.route("/api/games/offset/<offset>",methods=["GET"])
def api_games_offset(offset):
	games_list = []
	#return jsonify(Game.query.get(45).serialize())
	target = 25*(int(offset)-1)
	counter = 0
	found = 1
	games = Game.query.order_by(Game.id).limit(25).offset(target).all();
	for game in games:
		games_list.append(game.serialize_table())
	# print("Making sure it is going through this code")
	# for i in range (0,600000):
	# 	game = Game.query.get(i)
	# 	if game is None:
	# 		continue
	# 	if counter < target:
	# 		counter+=1
	# 		continue
	# 	dict_p[game.name] = game.serialize_table()
	# 	if found >= 25:
	# 		break
	# 	found +=1
	return jsonify(games_list)
	
	"""
	for data in Game.query:
		return jsonify({data.name: data.serialize_table()})
		counter += 1
		if counter < int(10*(int(offset)-1)):
			continue
		new_count+=1
		#print("New_count"+str(new_count))
		#print(int(data.id))
		
		dict_p[data.name] = data.serialize_table()
		if new_count > (10*(int(offset)-1) + 9):
	
			break
	return jsonify(dict_p)
	"""

@app.route('/api/games/<id>')
def api_games_id(id):
	return jsonify(Game.query.get(id).serialize())

@app.route('/api/characters/offset/<offset>')
def api_characters_offset(offset):
	character_list = []
	target = 25*(int(offset)-1)
	counter = 0
	found = 1
	characters = Character.query.order_by(Character.id).limit(25).offset(target).all();
	for character in characters:
		character_list.append(character.serialize_table())
	# for i in range (0,600000):
	# 	game = Character.query.get(i)
	# 	if game is None:
	# 		continue
	# 	if counter < target:
	# 		counter+=1
	# 		continue
	# 	dict_p[game.name] = game.serialize_table()
	# 	if found >= 25:
	# 		break
	# 	found +=1
	return jsonify(character_list)
@app.route('/api/characters/<id>')
def api_characters_id(id):
	return jsonify(Character.query.get(id).serialize())

@app.route('/api/platforms/offset/<offset>')
def api_platforms_offset(offset):
	games_list = []
	#return jsonify(Game.query.get(45).serialize())
	target = 25*(int(offset)-1)
	counter = 0
	found = 1
	games = Platform.query.order_by(Platform.id).limit(25).offset(target).all();
	for game in games:
		games_list.append(game.serialize_table())
	# print("Making sure it is going through this code")
	# for i in range (0,600000):
	# 	game = Game.query.get(i)
	# 	if game is None:
	# 		continue
	# 	if counter < target:
	# 		counter+=1
	# 		continue
	# 	dict_p[game.name] = game.serialize_table()
	# 	if found >= 25:
	# 		break
	# 	found +=1
	return jsonify(games_list)
	"""
	dict_p = {}
	
	counter = 0
	new_count = 25*(int(offset)-1)
	for data in Platform.query:
		counter += 1
		if counter < int(25*(int(offset)-1)):
			continue
		new_count+=1
		#print("New_count"+str(new_count))
		dict_p[data.name] = data.serialize_table()
		if new_count > (25*(int(offset)-1) + 24):
			break

	return jsonify(dict_p)
	
	target = 25*(int(offset)-1)
	counter = 0
	found = 1
	#platforms = Platform.query.filter(Platform.name.like('%do%')).limit(25)
	platforms = Platform.query.order_by(Platform.id).limit(25).offset(target).all();
	for platform in platforms:
		dict_p[platform.name] = platform.serialize_table()
	# print("Making sure it is going through this code")
	# for i in range (0,600000):
	# 	game = Character.query.get(i)
	# 	if game is None:
	# 		continue
	# 	if counter < target:
	# 		counter+=1
	# 		continue
	# 	dict_p[game.name] = game.serialize_table()
	# 	if found >= 25:
	# 		break
	# 	found +=1
	return jsonify(dict_p)
	"""
	

@app.route('/api/platforms/<id>')
def api_platforms_id(id):
	return jsonify(Platform.query.get(id).serialize())

@app.route('/search/result/games/<text>')
def search_result_games(text):
	#Basic search algorithm
	returnlist = []
	games_query = search(Game.query, text).limit(15)
	for game in games_query.all():
		search_result = SearchResult(game.id, game.name, "game", text)
		returnlist.append(search_result.toJSON())

	return jsonify(returnlist)
	"""
	query = search(query, 'first')
	print query.first().name
	"""
	#Nathan, what you'll want to do is run seach over all of these query and add the result together and jsonify and shit

@app.route('/search/result/characters/<text>')
def search_result_characters(text):
	#Basic search algorithm
	returnlist = []
	characters_query = search(Character.query, text).limit(15)
	for character in characters_query.all():
		search_result = SearchResult(character.id, character.name, "character", text)
		returnlist.append(search_result.toJSON())
	return jsonify(returnlist)

@app.route('/search/result/platforms/<text>')
def search_result_platforms(text):
	#Basic search algorithm
	returnlist = []
	platforms_query = search(Platform.query, text).limit(15)
	for platform in platforms_query.all():
		search_result = SearchResult(platform.id, platform.name, "platform", text)
		returnlist.append(search_result.toJSON())
	return jsonify(returnlist)

@app.route('/search/result/all/<text>')
def search_result_all(text):
	#Basic search algorithm
	returnlist = []
	games_query = search(Game.query, text).limit(15)
	characters_query = search(Character.query, text).limit(15)
	platforms_query = search(Platform.query, text).limit(15)

	for game in games_query.all():
		search_result = SearchResult(game.id, game.name, "game", text)
		returnlist.append(search_result.toJSON())

	for character in characters_query.all():
		search_result = SearchResult(character.id, character.name, "character", text)
		returnlist.append(search_result.toJSON())

	for platform in platforms_query.all():
		search_result = SearchResult(platform.id, platform.name, "platform", text)
		returnlist.append(search_result.toJSON())

	return jsonify(returnlist)

	"""
	search_text = '%'+text+'%'
	returnlist = []
	games = Game.query.filter(Game.name.like('search_text')).limit(25).all()
	for game in games:
		dict_game = {"pillar": "game", "name": game.name, "id": game.id}
		returnlist.append(dict_game)
	characters = Character.query.filter(Character.name.like(search_text)).limit(25)
	for character in characters:
		dict_game = {"pillar": "character", "name": character.name, "id": character.id}
		returnlist.append(dict_game)
	platforms = Platform.query.filter(Platform.name.like(search_text)).limit(25)
	for platform in platforms:
		dict_game = {"pillar": "platform", "name": platform.name, "id": platform.id}
		returnlist.append(dict_game)
	return jsonify(returnlist)
	"""




@app.route('/api/runtests')
def api_runtests():
	output = runTestsOut()
	if not output:
		output = "HELLLOOO"
	return output

def shell_context():
	context = {
		'app': app,
		'db': db,
		'Game': Game,
		'Platforms':Platform,
		'Characters':Characters
	}
	return context

manager.add_command('shell', Shell(make_context=shell_context))

if __name__ == "__main__":
	manager.run()

