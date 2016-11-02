#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import json
from models import Game, Platform, Character






"""
#Code to load up temp data from JSON files
gameDict = dict()
for x in range(1,4):
	with open('static/json/game'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		gameDict[data['id']] = data

characterDict = {}
for x in range(1,4):
	with open('static/json/character'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		characterDict[data['id']] = data

platformDict = dict()
for x in range(1,4):
	with open('static/json/platform'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		platformDict[data['id']] = data
"""
gameDict = dict()
for x in range(1,56877):
	b = Game.query.filter_by(id = i).first()
	if b is None:
		continue
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

@app.route('/api/games/')
def api_games_all():
	return jsonify( dict(data.name, data.serialize()) for data in Game.query )

@app.route('/api/games/<id>')
def api_game_id(id):
	return jsonify(Game.query.get(id).serialize())

@app.route('/api/characters')
def api_characters_all():
	return jsonify( dict(data.name, data.serialize()) for data in Character.query )

@app.route('/api/characters/<id>')
def api_characters_id(id):
	return jsonify(Character.query.get(id).serialize())

@app.route('/api/platforms')
def api_platforms_all():
	return jsonify( dict(data.name, data.serialize()) for data in Platform.query )

@app.route('/api/platforms/<id>')
def api_platforms_id(id):
	return jsonify(Platform.query.get(id).serialize())

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

