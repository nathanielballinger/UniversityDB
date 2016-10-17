from flask import Flask, send_file, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)
manager = Manager(app)

#Many to many relationship table between characters and games
#char_game = db.Table('char_game', db.Column('character_id', db.Integer, db.ForeignKey('Character.id'),db.column('game_id',db.Integer,db.ForeignKey('Game.id'))))

#Many to many relationship table between games and platforms
#plat_game = db.Table('plat_game', db.Column('character_id', db.Integer, db.ForeignKey('character.id'),db.column('platform_id',db.Integer,db.ForeignKey('platform.id'))))

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
	#Image
	#Define relationship with platforms. Links to table. Backref creates new property of platforms that list all games
	#platforms = db.relationship('Platform', secondary = plat_game, backref = db.backref('games'))
	#characters = db.relationship('Character', secondary = char_game, backref = db.backref('games'))

	aliases = db.Column(db.String)
	site_detail_url = db.Column(db.String)


	def __repr__(self):
		return '<Game>'

class Platform(db.Model):
	__tablename__ = 'platform'
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
	#Image


	def __repr__(self):
		return '<Platform>'

class Character(db.Model):
	__tablename__ = 'characters'
	#Column values are name, birthday, gender, deck, game first appeared in
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	birthday = db.Column(db.String)
	gender = db.Column(db.String)
	deck = db.Column(db.String)
	game_first_appeared = db.relationship('Game', )
	#Page Values are Description, Image, Site_Detail_URL, aliases
	description = db.Column(db.String)
	#Image
	site_detail_url = db.Column(db.String)
	aliases = db.Column(db.String)

	def __repr__(self):
		return '<Character>'


@app.route("/")
def index():
	return send_file("templates/index.html")

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
