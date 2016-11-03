#!/usr/bin/python3.5
from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import json
import re
#Only add app. on the next two lines when you want to run the DO server
import app. models
from app.models import Game, Character, Platform

Base = declarative_base()
app = Flask(__name__)
#Chris's DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe2'
#Digital Ocean DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gusman772:MrSayanCanSing2@localhost:5432/swe'

db = SQLAlchemy(app)
manager = Manager(app)




#Checking to make sure we loaded the data correctly
for i in range(0,50):
	g = Game.query.filter_by(id = i).first()
	if g is None:
		print("###############################")
		print ("Game ID not found"+str(i))
		continue
	print("###################################")
	print(i)
	print (g)
	print(g.name)
	if (g.character is not None):
		print("Character =" + g.character)
	else:
		print("We got nothin")

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
	print(g.description)
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
	print(g.description)
	print(g.tiny_image)
	print(g.medium_image)
	print(g.site_detail_url)
	print(g.aliases)
	print(g.first_appeared_in_game)



"""
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
"""
for x in range(1,56877):
	b = Game.query.filter_by(id = i).first()
	if b is None:
		continue
"""
print("Does anything hapen")
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
	print("DID IT GET IN HERE?")
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

