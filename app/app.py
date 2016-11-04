#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import json
import time
import re
from tests import runTestsOut

#Only add app. on the next two lines when you want to run the DO server
import models

from models import Game, Character, Platform, db, Base, app, manager


#Checking to make sure we loaded the data correctly
# for i in range(0,50):
# 	g = Game.query.filter_by(id = i).first()
# 	if g is None:
# 		print("###############################")
# 		print ("Game ID not found"+str(i))
# 		continue
# 	print("###################################")
# 	print(i)
# 	print (g)
# 	print(g.name)
# 	if (g.character is not None):
# 		print("Character =" + g.character)
# 	else:
# 		print("We got nothin")
"""
for i in range(0,50):
	g = Platform.query.filter_by(id = i).first()
	if g is None:
		print("###############################")
		print ("Platform ID not found"+str(i))
		continue
	print("###################################")
	print(i)
	print (g)
	print(g.name)
	print(g.release_date)
	print(g.company)
	print(g.starting_price)
	print(g.install_base)
	#print(g.description)
	print(g.online_support)
	print(g.abbreviations)
	print(g.tiny_image)
	print(g.medium_image)
	print(g.site_detail_url)
	print(g.games)


for i in range(0,50):
	g = Character.query.filter_by(id = i).first()
	if g is None:
		print("###############################")
		print ("Character ID not found"+str(i))
		continue
	print("###################################")
	print(i)
	print (g)
	print(g.name)
	print(g.birthday)
	print(g.deck)
	#print(g.description)
	print(g.tiny_image)
	print(g.medium_image)
	print(g.site_detail_url)
	print(g.aliases)
	print("first_appeared"+str(g.first_appeared_in_game))


#Code to load up temp data from JSON files
gameDict = dict()
for x in range(1,4):
	with open('/var/www/cs373f-idb/app/static/json/game'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		gameDict[data['id']] = data
characterDict = {}
for x in range(1,4):
	with open('/var/www/cs373f-idb/app/static/json/character'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		characterDict[data['id']] = data
platformDict = dict()
for x in range(1,4):
	with open('/var/www/cs373f-idb/app/static/json/platform'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		platformDict[data['id']] = data

"""
gameDict = dict()
characterDict = dict()
platformDict = dict()




@app.route("/")
def index():
	return send_file("templates/index.html")



### -------------OUTDATED! USE API CALLS NOW----------- ###

#Get request for a list of all games
@app.route("/getGameTable/",methods=["GET"])
def getGameTable():
	obj = []
	for key, value in gameDict.items():
		obj.append(value)
	return jsonify(obj)

#Get request for a list of all platforms
@app.route("/getPlatformTable/",methods=["GET"])
def getPlatformTable():
	obj = []
	for key, value in platformDict.items():
		obj.append(value)
	return jsonify(obj)

#Get request for a list of all Characters
@app.route("/getCharacterTable/",methods=["GET"])
def getCharacterable():
	obj = []
	for key, value in characterDict.items():
		obj.append(value)
	return jsonify(obj)

#GET Request for a single Game
@app.route("/getGame/",methods=["GET"])
def getGame():
	game_id = int(request.args.get('id'))
	obj = jsonify(gameDict[game_id])
	return obj

#GET Request for a single character
@app.route("/getCharacter/",methods=["GET"])
def getCharacter():
	char_id = int(request.args.get('id'))
	obj = jsonify(characterDict[char_id])
	return obj
	
#GET Request for a single Platform
@app.route("/getPlatform/",methods=["GET"])
def getPlatform():
	platform_id = int(request.args.get('id'))
	obj = jsonify(platformDict[platform_id])
	return obj



### ------------------------------------------------- ###

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
def api_game_id(id):
	print("DID IT GET IN HERE?")
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
	
	dict_p = {}
	"""
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
	"""
	target = 25*(int(offset)-1)
	counter = 0
	found = 1
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
