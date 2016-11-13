#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_searchable import search
import json
import time
import re
from app.tests import runTestsOut

#Only add app. on the next two lines when you want to run the DO server
import app.models
from app.models import Game, Character, Platform, db, Base, app, manager

#Chris's DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe2'
#Digital Ocean DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gusman772:MrSayanCanSing2@localhost:5432/swe'
#Abhi's DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swe:asdfzxc@localhost:9000/swe'


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

@app.route('/api/games/offset/<offset>')
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
	

@app.route('/api/games/<id>')
def api_games_id(id):
	return jsonify(Game.query.get(id).serialize())

@app.route('/api/games/mapping')
def api_game_id(id):
	print("DID IT GET IN HERE?")
	games = Game.query.filter(Game.id.in_((2,3))).all()
	print(games)
	print(games.serialize_table())
	return jsonify(Game.query.filter(Game.id.in_((2,3))))

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


##Function to get a bunch of games from ID	
@app.route('/api/game_mapping/<ids>')
def api_characters_mapping(ids):
	id_list = ids.split(",")
	id_list = id_list[:-1]
	other_list = [int(x) for x in id_list]
	games = Game.query.filter(Game.id.in_(tuple(other_list))).all()
	id_dict = {}
	for game in games:
		temp = game.serialize_table()
		id_dict[temp['id']] = temp['name']
		# id_dict.append({temp['id']: temp['name']})
	return jsonify(id_dict)

#Function to get a bunch of platforms from IDS
@app.route('/api/platform_mapping/<ids>')
def api_platforms_mapping(ids):
	id_list = ids.split(",")
	id_list = id_list[:-1]
	other_list = [int(x) for x in id_list]
	platforms = Platform.query.filter(Platform.id.in_(tuple(other_list))).all()
	id_dict = []
	for platform in platforms:
		temp = platform.serialize_table()
		# id_dict[temp['id']] = temp['name']
		# id_dict.append({temp['id']: temp['name']})
		id_dict.append({"name": temp['name'], "id": temp['id']})
	return jsonify(id_dict)

#Function to get a bunch of characters from IDS
@app.route('/api/character_mapping/<ids>')
def api_games_mapping(ids):
	id_list = ids.split(",")
	id_list = id_list[:-1]
	other_list = [int(x) for x in id_list]
	characters = Character.query.filter(Character.id.in_(tuple(other_list))).all()
	id_dict = []
	for character in characters:
		temp = character.serialize_table()
		# id_dict[temp['id']] = temp['name']
		id_dict.append({"name": temp['name'], "id": temp['id']})
	return jsonify(id_dict)



@app.route('/api/characters/<id>')
def api_characters_id(id):
	return jsonify(Character.query.get(id).serialize())

@app.route('/api/platforms/offset/<offset>')
def api_platforms_offset(offset):
	
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
	

@app.route('/api/platforms/<id>')
def api_platforms_id(id):
	return jsonify(Platform.query.get(id).serialize())

@app.route('/search/result/<text>')
def search_result(text):
	#Basic search algorithm
	
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
	
	char_query = db.session.query(Character)
	plat_query = db.session.query(Platform)
	game_query = db.session.query(Game)

	"""
	query = search(query, 'first')
	print query.first().name
	"""
	#Nathan, what you'll want to do is run seach over all of these query and add the result together and jsonify and shit




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

