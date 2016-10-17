from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)
manager = Manager(app)
"""
class Book(db.Model):
	__tablename__ = 'books'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
	price = db.Column(db.Float)
	type = db.Column(db.String)

	def __repr__(self):
		return '<Book %r>' % self.title

class Author(db.Model):
	__tablename__ = 'authors'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	birth_date = db.Column(db.Date)
	bio = db.Column(db.Text)
	books = db.relationship('Book', backref='author')

	def __repr__(self):
		return '<Author %r>' % self.name
"""


class Game(db.Model):
	__tablename__ = 'games'
	#Column values are name, release date, genre, developers/publisher, rating of first release
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	release_date = db.Column(db.String)
	genre = db.Column(db.String)
	developers = db.Column(db.String)
	rating = db.Column(db.Float)

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
	game_first_appeared = db.Column(db.String)

	def __repr__(self):
		return '<Character>'


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/games/')
def games():
	b = Game.query.all()
	return render_template('games.html', games=b)

@app.route('/platforms')
def platforms():
	a = Platform.query.all()
	return render_template('platforms.html', platforms=a)

@app.route('/characters')
def characters():
	c = Character.query.all()
	return render_template('characters.html', characters=c)

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
