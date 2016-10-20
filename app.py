from flask import Flask, send_file, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from sqlalchemy.ext.declarative import declarative_base
import json
import urllib.request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)
manager = Manager(app)



#Code to load up temp data from JSON files
gameDict = dict()
for x in range(1,4):
	with open('static/json/game'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		gameDict[data['id']] = data

characterDict = dict()
for x in range(1,4):
	with open('static/json/character'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		characterDict[data['id']] = data

platformDict = dict()
for x in range(1,4):
	with open('static/json/platform'+str(x)+'.json') as data_file:
		data = json.load(data_file)['results']
		platformDict[data['id']] = data

#LINES  35 - 101 Are the SQLAlchemy Models
Base = declarative_base()
#Many to many relationship table between characters and games
char_game = db.Table(db.Column('char_id',db.Integer, db.ForeignKey('characters.id')),db.Column('game_id',db.Integer,db.ForeignKey('games.id')))

#Many to many relationship table between games and platforms
plat_game = db.Table(db.Column('character_id', db.Integer, db.ForeignKey('characters.id')),db.Column('platform_id',db.Integer,db.ForeignKey('platforms.id')))

class Game(db.Model):
	__tablename__ = 'games'
	#Column values are name, release date, genre, developers/publisher, rating of first release
	id = db.Column(db.Integer, primary_key=True)
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
	def __repr__(self):
		return '<Game %r>' % name

class Platform(db.Model):
	__tablename__ = 'platforms'
	#Column values are name, release date, company, starting price, number of sold units
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	release_date = db.Column(db.String)
	company = db.Column(db.String)
	starting_price = db.Column(db.String)
	number_units_sold = db.Column(db.Integer)
	#Page values are description, online support flag, abbreviations, site_detail_url, Image
	description = db.Column(db.String)
	online_support = db.Column(db.String)
	abbreviations = db.Column(db.String)
	site_detail_url = db.Column(db.String)
	image = db.Column(db.String)


	def __repr__(self):
		return '<Platform %r>' % name

class Character(db.Model):
	__tablename__ = 'characters'
	#Column values are name, birthday, gender, deck, game first appeared in
	id = db.Column(db.Integer, primary_key=True)
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

	def __repr__(self):
		return '<Character %r>' % name 


@app.route("/")
def index():
	return send_file("templates/index.html")


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

