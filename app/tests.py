from io             import StringIO
from unittest       import main, TestCase, TextTestRunner, makeSuite
#Only add app. before models when you want to run the DO server
from app.models 		import *

class TestCases (TestCase):

	# ------
	# Games
	# ------

	def test_case_game_1(self):
		game1 = Game("13328", "Wii Sports", "2006-11-19 00:00:00", \
			"Packaged with the Wii (except Japan), Wii Sports allows players to compete with friends in tennis, bowling, boxing, baseball, and golf.", \
			"http://www.giantbomb.com/api/image/square_mini/2280537-box_wiisp.png", "http://www.giantbomb.com/api/image/scale_medium/2280537-box_wiisp.png", \
			"PLATFORMS", None, "http://www.giantbomb.com/wii-sports/3030-13328/")

		self.assertEqual(game1.id, "13328")
		self.assertEqual(game1.release_date, "2006-11-19 00:00:00")
		self.assertEqual(game1.site_detail_url, "http://www.giantbomb.com/wii-sports/3030-13328/")

	def test_case_game_2(self):
		game2 = Game("52537", "LEGO Star Wars: The Force Awakens", "2016-06-28 00:00:00", \
			"LEGO Star Wars: The Force Awakens covers the seventh film and includes material that occurred between Return of the Jedi and Force Awakens.",\
			"http://www.giantbomb.com/api/image/square_mini/2822264-lswtfa.jpg", "http://www.giantbomb.com/api/image/scale_medium/2822264-lswtfa.jpg",\
			"PLATFORMS", None, "http://www.giantbomb.com/lego-star-wars-the-force-awakens/3030-52537/")

		self.assertEqual(game2.id, "52537")
		self.assertEqual(game2.tiny_image, "TINY_IMAGE")
		self.assertEqual(game2.aliases, None)

	def test_case_game_3(self):
		game3 = Game("41088", "Pokémon X/Y", "2013-10-12 00:00:00", \
			"The first Pokémon games on the 3DS and the first to be released simultaneously worldwide.", \
			"http://www.giantbomb.com/api/image/square_mini/2482818-pokemonxy.jpg", "http://www.giantbomb.com/api/image/scale_medium/2482818-pokemonxy.jpg",\
			"PLATFORMS", "Pokemon X/Y\nPokemon Y", "http://www.giantbomb.com/pokemon-xy/3030-41088/")

		self.assertEqual(game3.id, "41088")
		self.assertEqual(game3.tiny_image, "http://www.giantbomb.com/api/image/square_mini/2482818-pokemonxy.jpg")
		self.assertEqual(game3.name, "Pokémon X/Y")

	def test_case_game_4(self):
		game4 = Game("2133", "Call of Duty 4: Modern Warfare", "2007-11-05 00:00:00", \
			"Call of Duty 4: Modern Warfare ditches the World War II motif of the past Call of Duty games to tell a story set in contemporary times, and backs it up with a solid, feature-rich multiplayer mode.", \
			"http://www.giantbomb.com/api/image/square_mini/1875205-box_cod4.png", "http://www.giantbomb.com/api/image/scale_medium/1875205-box_cod4.png",\
			"PLATFORMS", "COD4, COD4: MW, Modern Warfare\n", "http://www.giantbomb.com/call-of-duty-4-modern-warfare/3030-2133/")

		self.assertEqual(game4.id, "2133")
		self.assertEqual(game4.release_date, "2007-11-05 00:00:00")
		self.assertEqual(game4.medium_image, "http://www.giantbomb.com/api/image/scale_medium/1875205-box_cod4.png")

	def test_case_game_5(self):
		game5 = Game(" "," "," "," "," "," "," "," "," "," "," ")

		self.assertEqual(game5.id, " ")
		self.assertEqual(game5.platforms, " ")
		self.assertEqual(game5.rating, " ")



	# ------
	# Platforms
	# ------

	def test_case_platform_1(self):
		platform1 = Platform("117", "Nintendo 3DS", "2011-02-26 00:00:00", "Nintendo", "249.00", "51630000", \
			"The Nintendo 3DS is a portable game console produced by Nintendo. The handheld features stereoscopic 3D technology that doesn't require glasses. It was released in Japan on February 26, 2011 and in North America on March 27, 2011.", \
			True, "3DS", "http://www.giantbomb.com/nintendo-3ds/3045-117/",\
			"http://www.giantbomb.com/api/image/square_mini/1686079-3dshw11911.jpg", "http://www.giantbomb.com/api/image/scale_medium/1686079-3dshw11911.jpg")

		self.assertEqual(platform1.id, "117")
		self.assertEqual(platform1.name, "Nintendo 3DS")
		self.assertEqual(platform1.release_date, "2011-02-26 00:00:00")

	def test_case_platform_2(self):
		platform2 = Platform("20", "Xbox 360", "2005-11-22 00:00:00", "Microsoft Studios", "399.00", "80000000", \
			"The Xbox 360 is the second game console produced by Microsoft Corporation and is the successor to the original Xbox.", \
			True, "360\nXenon", "http://www.giantbomb.com/xbox-360/3045-20/",\
			"http://www.giantbomb.com/api/image/square_mini/195092-xbox_360_console_02.jpg", "http://www.giantbomb.com/api/image/scale_medium/195092-xbox_360_console_02.jpg")

		self.assertEqual(platform2.id, "20")
		self.assertEqual(platform2.tiny_image, "http://www.giantbomb.com/api/image/square_mini/195092-xbox_360_console_02.jpg")
		self.assertEqual(platform2.starting_price, "399.00")

	def test_case_platform_3(self):
		platform3 = Platform("35", "PlayStation 3", "2006-11-11 00:00:00", "Sony Interactive Entertainment", "599.00", "80000000", \
			"The PlayStation 3 (often abbreviated PS3) is the third home video game console created and released by Sony Computer Entertainment Inc.", \
			True, "PS3", "http://www.giantbomb.com/playstation-3/3045-35/",\
			"http://www.giantbomb.com/api/image/square_mini/1426360-logo.jpg", "http://www.giantbomb.com/api/image/scale_medium/1426360-logo.jpg")

		self.assertEqual(platform3.id, "35")
		self.assertEqual(platform3.install_base, "80000000")
		self.assertEqual(platform3.company, "Sony Interactive Entertainment")

	def test_case_platform_4(self):
		platform4 = Platform("146", "PlayStation4", "2013-11-15 00:00:00", "Sony Interactive Entertainment", "399.00", "40000000", \
			"PlayStation 4 is Sony's fourth home video game console, released on November 15, 2013 in North America, and November 29, 2013 in Europe.", \
			True, "PS4\r\nOrbis", "http://www.giantbomb.com/playstation-4/3045-146/",\
			"http://www.giantbomb.com/api/image/square_mini/2495936-9012444134_80ba47fd6e_o.jpg", "http://www.giantbomb.com/api/image/scale_medium/2495936-9012444134_80ba47fd6e_o.jpg")

		self.assertEqual(platform4.id, "146")
		self.assertEqual(platform4.medium_image, "http://www.giantbomb.com/api/image/scale_medium/2495936-9012444134_80ba47fd6e_o.jpg")
		self.assertEqual(platform4.name, "PlayStation 4")

	def test_case_platform_5(self):
		platform5 = Platform(" "," "," "," "," "," "," "," "," "," "," ")
		
		self.assertEqual(platform5.id," ")
		self.assertEqual(platform5.starting_price, " ")
		self.assertEqual(platform5.name," ")

	# ------
	# Characters
	# ------

	def test_case_character_1(self):
		character1 = Character("2", "Sub-Zero", None, "1", \
			"Kuai Liang, known as Tundra, became an assassin for the Lin Kuei after he and his brother were abducted by the clan. After the death of his brother Bi Han, Kuai Liang assumed the mantle of Sub-Zero to honor his memory.", \
			"Sub-Zero is a video game character from the Mortal Kombat series and one of the original characters in the first Mortal Kombat game in 1992. A mainstay of the series, Sub-Zero is the only character who has appeared in every main Mortal Kombat fighting game. The character also appears in many other Mortal Kombat media works such as the Mortal Kombat live action film series and animated series.", \
			"http://www.giantbomb.com/api/image/square_mini/2663932-cds.jpeg", "http://www.giantbomb.com/api/image/scale_medium/2663932-cds.jpeg", \
			"http://www.giantbomb.com/sub-zero/3005-2/", "LK-520\r\nTundra\r\nCyber Sub-Zero\r\nKuai Liang", "25042")

		self.assertEqual(character1.id, "2")
		self.assertEqual(character1.name, "Sub-Zero")
		self.assertEqual(character1.gender, "1")

	def test_case_character_2(self):
		character2 = Character("177", "Mario", "Jun 2, 1981", "1", \
			"Originally a carpenter named Jumpman, this Italian plumber has gone on to become the most recognizable video game character of them all, starring in a veritable pantheon of titles like kart racing and sports. He has been voiced by Charles Martinet for nearly 20 years.", \
			"Mario is a fictional character in the Mario video game franchise, owned by Nintendo and created by video game designer Shigeru Miyamoto. Serving as the company's mascot and the eponymous protagonist of the series, Mario has appeared in over 200 video games since his creation. Depicted as a short, pudgy, Italian plumber who resides in the Mushroom Kingdom, his adventures generally center upon rescuing Princess Peach from the Koopa villain Bowser. His younger brother is Luigi.", \
			"http://www.giantbomb.com/api/image/square_mini/2555000-2339414779-Mario.png", "http://www.giantbomb.com/api/image/scale_medium/2555000-2339414779-Mario.png", \
			"http://www.giantbomb.com/mario/3005-177/", "Jumpman\r\nBaby Mario", "311")

		self.assertEqual(character2.id, "177")
		self.assertEqual(character2.game_first_appeared, "311")
		self.assertEqual(character2.tiny_image, "http://www.giantbomb.com/api/image/square_mini/2555000-2339414779-Mario.png")

	def test_case_character_3(self):
		character3 = Character("5766", "Brock", "1", \
			"\"The Rock-Solid Pokémon Trainer!\"", \
			"Brock is a fictional character in the Pokémon franchise owned by Nintendo. In the Pokémon video games, he is the Gym Leader of Pewter City and mainly uses Rock-type Pokémon. In the anime series, Ash comes across a man that is later revealed to be Brock's father. He explains that Brock wanted to become a Pokémon Master but due to his father leaving, Brock had to take care of his many, many siblings and could not leave. This is why he became a gym leader, to stay close to his family. His father comes back and states he will take care of the family. Brock left his position as a Gym Leader to travel alongside Ash Ketchum and became a revered Pokémon Breeder. He later cultivates his skill in medicine. As of the latest Japanese episode, Brock is at Pewter City to train to be a Pokémon Doctor.", \
			"http://www.giantbomb.com/api/image/square_mini/1906766-pokemon_heartgold_soulsilver_brock.png", "http://www.giantbomb.com/api/image/scale_medium/1906766-pokemon_heartgold_soulsilver_brock.png", \
			"http://www.giantbomb.com/brock/3005-5766/", None, "3966")

		self.assertEqual(character3.id, "5766")
		self.assertEqual(character3.name, "Brock")
		self.assertEqual(character3.game_first_appeared, "3966")

	def test_case_character_4(self):
		character4 = Character(" "," "," "," "," "," "," "," "," "," ")
		
		self.assertEqual(character4.id, " ")
		self.assertEqual(character4.name, " ")
		self.assertEqual(character4.game_first_appeared, " ")

	# ------
	# Other Tests
	# ------

	def test_game_serialize_1(self):
		obj = Game("13328", "Wii Sports", "2006-11-19 00:00:00", \
			"Packaged with the Wii (except Japan), Wii Sports allows players to compete with friends in tennis, bowling, boxing, baseball, and golf.", \
			"http://www.giantbomb.com/api/image/square_mini/2280537-box_wiisp.png", "http://www.giantbomb.com/api/image/scale_medium/2280537-box_wiisp.png", \
			"PLATFORMS", None, "http://www.giantbomb.com/wii-sports/3030-13328/")
		obj.serialize()
		test = {'id': "13328", 'name': "Wii Sports", 'release_date': "2006-11-19 00:00:00", \
		'description': "Packaged with the Wii (except Japan), Wii Sports allows players to compete with friends in tennis, bowling, boxing, baseball, and golf.", \
		'tiny_image': "http://www.giantbomb.com/api/image/square_mini/2280537-box_wiisp.png", 'medium_image': "http://www.giantbomb.com/api/image/scale_medium/2280537-box_wiisp.png", \
		'platforms': "PLATFORMS", 'aliases': None, 'site_detail_url': "http://www.giantbomb.com/wii-sports/3030-13328/"}
		self.assertEqual(obj, test)



# ----
# Main
# ----

if __name__ == '__main__' :
	main()

def runTestsOut():
	stream = StringIO()
	runner = TextTestRunner(stream=stream)
	result = runner.run(makeSuite(TestCases))
	stream.seek(0)
	return stream.read()

