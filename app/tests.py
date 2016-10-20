from io             import StringIO
from urllib.request import urlopen
from unittest       import main, TestCase
from models 		import *
import json, postgresql

class TestCases (TestCase):

	# ------
	# Games
	# ------

	def test_case_game_1(self):
		game1 = Game(13328, "Wii Sports", "11/19/2006", "Sports", "Nintendo EAD", "3.65", \
			"Wii Sports is the pack-in for the Wii for all regions except for Japan. It includes five sports mini-games, corresponding challenges, and a daily trainer that gives the player a score similar to the Brain Age system. It utilizes Miis as the player's avatar.", \
			"REVIEW", "IMAGE", "Wii", "Mii")

		self.assertEqual(game1.id, 13328)
		self.assertEqual(game1.release_date, "11/19/2006")
		self.assertEqual(game1.platforms, "Wii")

	def test_case_game_2(self):
		game2 = Game(52537, "LEGO Star Wars: The Force Awakens", "06/28/2016", "{Sci-Fi, Comedy}",
			"WB Games", "3", 
			"The fifth title in the LEGO Star Wars franchise and the first developed since The Walt Disney Company acquired Lucasfilm. The game adapts the characters and events depicted in the film Star Wars: The Force Awakens as well as new material set after Return of the Jedi leading up to The Force Awakens. The game was announced on February 2nd 2016 with a trailer parodying the film's first teaser trailer.",
			"REVIEW", "IMAGE", "Xbox 360", "Rey")

		self.assertEqual(game2.id, 52537)
		self.assertEqual(game2.rating, "3")
		self.assertEqual(game2.developers, "WB Games")