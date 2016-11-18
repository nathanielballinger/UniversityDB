from io             import StringIO
from unittest       import main, TestCase, TextTestRunner, makeSuite
#Only add app. before models when you want to run the DO server
from models 		import *

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
		self.assertEqual(game2.tiny_image, "http://www.giantbomb.com/api/image/square_mini/2822264-lswtfa.jpg")
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
		game5 = Game("48805", "American Truck Simulator", "2016-02-02 00:00:00", \
			"The latest truck driving simulator in development by SCS Software.", \
			"http://www.giantbomb.com/api/image/square_mini/2843071-3730221427-Ameri.jpg", "http://www.giantbomb.com/api/image/scale_medium/2843071-3730221427-Ameri.jpg", \
			"PLATFORMS", None, "http://www.giantbomb.com/american-truck-simulator/3030-48805/")

		self.assertEqual(game5.id, "48805")
		self.assertEqual(game5.name, "American Truck Simulator")
		self.assertEqual(game5.site_detail_url, "http://www.giantbomb.com/american-truck-simulator/3030-48805/")

	def test_case_game_6(self):
		game6 = Game(" "," "," "," "," "," "," "," "," ")

		self.assertEqual(game6.id, " ")
		self.assertEqual(game6.platforms, " ")
		self.assertEqual(game6.medium_image, " ")


	def test_case_game_7(self):
		db.session.rollback()
		game7 = Game("600000", "Test Game", "2016-11-03 00:00:00", "Test Description", "http://www.redbackconferencing.com.au/2016/lobby/success-blue-transparent.png", \
            "http://www.velior.ru/wp-content/uploads/2009/05/Test-Computer-Key-by-Stuart-Miles.jpg", \
            "Test Platform", "TGame", "http://www.giantbomb.com/call-of-duty-4-modern-warfare/3030-2133")

		dbgame = Game.query.get(600000)
		if dbgame is not None:
			db.session.delete(dbgame)
			db.session.commit()


		db.session.add(game7)
		db.session.commit()
		dbgame = Game.query.get(600000)
		self.assertEqual(dbgame.id, 600000)

		db.session.delete(dbgame)
		db.session.commit()

	def test_case_game_8(self):
		db.session.rollback()
		game8 = Game("600000", "Test Game", "2016-11-03 00:00:00", "Test Description", "http://www.redbackconferencing.com.au/2016/lobby/success-blue-transparent.png", \
            "http://www.velior.ru/wp-content/uploads/2009/05/Test-Computer-Key-by-Stuart-Miles.jpg", \
            "Test Platform", "TGame", "http://www.giantbomb.com/call-of-duty-4-modern-warfare/3030-2133")

		dbgame = Game.query.get(600000)
		if dbgame is not None:
			db.session.delete(dbgame)
			db.session.commit()

		db.session.add(game8)
		db.session.commit()
		db.session.delete(game8)
		db.session.commit()

		self.assertTrue(Game.query.get(600000) is None)



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
		platform4 = Platform("146", "PlayStation 4", "2013-11-15 00:00:00", "Sony Interactive Entertainment", "399.00", "40000000", \
			"PlayStation 4 is Sony's fourth home video game console, released on November 15, 2013 in North America, and November 29, 2013 in Europe.", \
			True, "PS4\r\nOrbis", "http://www.giantbomb.com/playstation-4/3045-146/",\
			"http://www.giantbomb.com/api/image/square_mini/2495936-9012444134_80ba47fd6e_o.jpg", "http://www.giantbomb.com/api/image/scale_medium/2495936-9012444134_80ba47fd6e_o.jpg")

		self.assertEqual(platform4.id, "146")
		self.assertEqual(platform4.medium_image, "http://www.giantbomb.com/api/image/scale_medium/2495936-9012444134_80ba47fd6e_o.jpg")
		self.assertEqual(platform4.name, "PlayStation 4")

	def test_case_platform_5(self):
		platform5 = Platform(" "," "," "," "," "," "," "," "," "," "," "," ")
		
		self.assertEqual(platform5.id," ")
		self.assertEqual(platform5.starting_price, " ")
		self.assertEqual(platform5.name," ")

	def test_case_platform_6(self):
		db.session.rollback()
		platform = Platform("600000", "Test Platform",  "2016-11-03 00:00:00", "Company", "50", "50000", "Description", True, "abbr.", "URL", "Tiny", "Medium")

		dbplat = Platform.query.get(600000)
		if dbplat is not None:
			db.session.delete(dbplat)
			db.session.commit()

		db.session.add(platform)
		db.session.commit()
		dbplatform = Platform.query.get(600000)
		self.assertEqual(dbplatform.id, 600000)

		db.session.delete(dbplatform)
		db.session.commit()

	def test_case_platform_7(self):
		db.session.rollback()
		platform = Platform("600000", "Test Platform",  "2016-11-03 00:00:00", "Company", "50", "50000", "Description", True, "abbr.", "URL", "Tiny", "Medium")

		dbplat = Platform.query.get(600000)
		if dbplat is not None:
			db.session.delete(dbplat)
			db.session.commit()


		db.session.add(platform)
		db.session.commit()
		db.session.delete(platform)
		db.session.commit()

		self.assertTrue(Platform.query.get(600000) is None)

	# ------
	# Characters
	# ------

	def test_case_character_1(self):
		character1 = Character("2", "Sub-Zero", None, "1", \
			"Kuai Liang, known as Tundra, became an assassin for the Lin Kuei after he and his brother were abducted by the clan. After the death of his brother Bi Han, Kuai Liang assumed the mantle of Sub-Zero to honor his memory.", \
			"DESCRIPTION", \
			"http://www.giantbomb.com/api/image/square_mini/2663932-cds.jpeg", "http://www.giantbomb.com/api/image/scale_medium/2663932-cds.jpeg", \
			"http://www.giantbomb.com/sub-zero/3005-2/", "LK-520\r\nTundra\r\nCyber Sub-Zero\r\nKuai Liang", "25042")

		self.assertEqual(character1.id, "2")
		self.assertEqual(character1.name, "Sub-Zero")
		self.assertEqual(character1.gender, "1")

	def test_case_character_2(self):
		character2 = Character("177", "Mario", "Jun 2, 1981", "1", \
			"Originally a carpenter named Jumpman, this Italian plumber has gone on to become the most recognizable video game character of them all, starring in a veritable pantheon of titles like kart racing and sports. He has been voiced by Charles Martinet for nearly 20 years.", \
			"DESCRIPTION", \
			"http://www.giantbomb.com/api/image/square_mini/2555000-2339414779-Mario.png", "http://www.giantbomb.com/api/image/scale_medium/2555000-2339414779-Mario.png", \
			"http://www.giantbomb.com/mario/3005-177/", "Jumpman\r\nBaby Mario", "311")

		self.assertEqual(character2.id, "177")
		self.assertEqual(character2.first_appeared_in_game, "311")
		self.assertEqual(character2.tiny_image, "http://www.giantbomb.com/api/image/square_mini/2555000-2339414779-Mario.png")

	def test_case_character_3(self):
		character3 = Character("5766", "Brock", None, "1", \
			"\"The Rock-Solid Pokémon Trainer!\"", \
			"DESCRIPTION", \
			"http://www.giantbomb.com/api/image/square_mini/1906766-pokemon_heartgold_soulsilver_brock.png", "http://www.giantbomb.com/api/image/scale_medium/1906766-pokemon_heartgold_soulsilver_brock.png", \
			"http://www.giantbomb.com/brock/3005-5766/", None, "3966")

		self.assertEqual(character3.id, "5766")
		self.assertEqual(character3.name, "Brock")
		self.assertEqual(character3.first_appeared_in_game, "3966")

	def test_case_character_4(self):
		character4 = Character("14816", "Amumu, the Sad Mummy", None, None, \
			"DESCRIPTION", \
			"http://www.giantbomb.com/api/image/square_mini/1334831-312e302e302e38322d3332.jpg", "http://www.giantbomb.com/api/image/scale_medium/1334831-312e302e302e38322d3332.jpg", \
			"http://www.giantbomb.com/amumu-the-sad-mummy/3005-14816/", None, " ","24024")

		self.assertEqual(character4.id, "14816")
		self.assertEqual(character4.first_appeared_in_game, "24024")
		self.assertEqual(character4.name, "Amumu, the Sad Mummy")

	def test_case_character_5(self):
		character5 = Character(" "," "," "," "," "," "," "," "," "," ", " ")
		
		self.assertEqual(character5.id, " ")
		self.assertEqual(character5.name, " ")
		self.assertEqual(character5.first_appeared_in_game, " ")

	def test_case_character_6(self):
		db.session.rollback()
		char = Character("600000", "Test Char", "Born on", 0, "deck", "description", "tiny", "medium", "url", "aliases", 1)

		dbchar = Character.query.get(600000)
		if dbchar is not None:
			db.session.delete(dbchar)
			db.session.commit()

		db.session.add(char)
		db.session.commit()
		dbchar = Character.query.get(600000)
		self.assertEqual(dbchar.id, 600000)

		db.session.delete(dbchar)
		db.session.commit()
	
	def test_case_character_7(self):
		db.session.rollback()
		char = Character("600000", "Test Char", "Born on", 0, "deck", "description", "tiny", "medium", "url", "aliases", 1)

		dbchar = Character.query.get(600000)
		if dbchar is not None:
			db.session.delete(dbchar)
			db.session.commit()

		db.session.add(char)
		db.session.commit()
		db.session.delete(char)
		db.session.commit()

		self.assertTrue(Character.query.get(600000) is None)

	# ------
	# SearchResults
	# ------

	def test_case_searchResult_1(self):
		searchResult1 = SearchResult(1, "Search 1", "Game", "Mario")

		self.assertEqual(searchResult1.id, 1)
		self.assertEqual(searchResult1.pillar, "Game")

	def test_case_searchResult_2(self):
		searchResult2 = SearchResult(2, "Search 2", "Platform", "Nintendo")

		self.assertEqual(searchResult2.id, 2)
		self.assertEqual(searchResult2.pillar, "Platform")

	def test_case_searchResult_3(self):
		searchResult3 = SearchResult(3, "Search 3", "Character", "Brock")

		self.assertEqual(searchResult3.id, 3)
		self.assertEqual(searchResult3.pillar, "Character")

	def test_case_searchResult_4(self):
		searchResult4 = SearchResult(" ", " ", " ", " ")

		self.assertEqual(searchResult4.id, " ")
		self.assertEqual(searchResult4.pillar, " ")

	def test_case_searchResult_5(self):
		searchResult4 = SearchResult(1, "Name", "Game", "Pokemon")

		self.assertEqual(searchResult4.id, 1)
		self.assertEqual(searchResult4.name, "Name")
		self.assertEqual(searchResult4.pillar, "Game")
		self.assertEqual(searchResult4._filteredSearchText, "pokemon")

	def test_case_searchResult_6(self):
		searchResult4 = SearchResult(45, " ", "Platform", "mArio and sonic")

		self.assertEqual(searchResult4.id, 45)
		self.assertEqual(searchResult4.name, " ")
		self.assertEqual(searchResult4.pillar, "Platform")
		self.assertEqual(searchResult4._filteredSearchText, "mario and sonic")

	# ------
	# Game Serialize
	# ------

	def test_game_serialize_1(self):
		obj = Game("13328", "Wii Sports", "2006-11-19 00:00:00", \
			"Packaged with the Wii (except Japan), Wii Sports allows players to compete with friends in tennis, bowling, boxing, baseball, and golf.", \
			"http://www.giantbomb.com/api/image/square_mini/2280537-box_wiisp.png", "http://www.giantbomb.com/api/image/scale_medium/2280537-box_wiisp.png", \
			"PLATFORMS", None, "http://www.giantbomb.com/wii-sports/3030-13328/")
		obj = obj.serialize()
		test = {'id': "13328", 'name': "Wii Sports", 'release_date': "2006-11-19 00:00:00", \
		'description': "Packaged with the Wii (except Japan), Wii Sports allows players to compete with friends in tennis, bowling, boxing, baseball, and golf.", \
		'tiny_image': "http://www.giantbomb.com/api/image/square_mini/2280537-box_wiisp.png", 'medium_image': "http://www.giantbomb.com/api/image/scale_medium/2280537-box_wiisp.png", \
		'platforms': [], 'aliases': None, 'site_detail_url': "http://www.giantbomb.com/wii-sports/3030-13328/", 'character': None, 'search_vector': None}
		self.assertEqual(obj, test)

	def test_game_serialize_2(self):
		obj = Game("52537", "LEGO Star Wars: The Force Awakens", "2016-06-28 00:00:00", \
			"LEGO Star Wars: The Force Awakens covers the seventh film and includes material that occurred between Return of the Jedi and Force Awakens.",\
			"http://www.giantbomb.com/api/image/square_mini/2822264-lswtfa.jpg", "http://www.giantbomb.com/api/image/scale_medium/2822264-lswtfa.jpg",\
			"PLATFORMS", None, "http://www.giantbomb.com/lego-star-wars-the-force-awakens/3030-52537/")
		obj = obj.serialize()
		test = {'id': "52537", 'name': "LEGO Star Wars: The Force Awakens", 'release_date': "2016-06-28 00:00:00", \
		'description': "LEGO Star Wars: The Force Awakens covers the seventh film and includes material that occurred between Return of the Jedi and Force Awakens.", \
		'tiny_image': "http://www.giantbomb.com/api/image/square_mini/2822264-lswtfa.jpg", 'medium_image': "http://www.giantbomb.com/api/image/scale_medium/2822264-lswtfa.jpg", \
		'platforms': [], 'aliases': None, 'site_detail_url': "http://www.giantbomb.com/lego-star-wars-the-force-awakens/3030-52537/", 'character': None, 'search_vector': None}
		self.assertEqual(obj, test)

	def test_game_serialize_3(self):
		obj = Game("41088", "Pokémon X/Y", "2013-10-12 00:00:00", \
			"The first Pokémon games on the 3DS and the first to be released simultaneously worldwide.", \
			"http://www.giantbomb.com/api/image/square_mini/2482818-pokemonxy.jpg", "http://www.giantbomb.com/api/image/scale_medium/2482818-pokemonxy.jpg",\
			"PLATFORMS", "Pokemon X/Y\nPokemon Y", "http://www.giantbomb.com/pokemon-xy/3030-41088/")
		obj = obj.serialize()
		test = {'id': "41088", 'name': "Pokémon X/Y", 'release_date': "2013-10-12 00:00:00", \
		'description': "The first Pokémon games on the 3DS and the first to be released simultaneously worldwide.", \
		'tiny_image': "http://www.giantbomb.com/api/image/square_mini/2482818-pokemonxy.jpg", 'medium_image': "http://www.giantbomb.com/api/image/scale_medium/2482818-pokemonxy.jpg", \
		'platforms': [], 'aliases': "Pokemon X/Y\nPokemon Y", 'site_detail_url': "http://www.giantbomb.com/pokemon-xy/3030-41088/", 'character': None, 'search_vector': None}
		self.assertEqual(obj, test)

	# ------
	# Serialize_Table for each object
	# ------

	def test_game_serialize_table_1(self):
		obj = Game("52537", "LEGO Star Wars: The Force Awakens", "2016-06-28 00:00:00", \
			"LEGO Star Wars: The Force Awakens covers the seventh film and includes material that occurred between Return of the Jedi and Force Awakens.",\
			"http://www.giantbomb.com/api/image/square_mini/2822264-lswtfa.jpg", "http://www.giantbomb.com/api/image/scale_medium/2822264-lswtfa.jpg",\
			"PLATFORMS", None, "http://www.giantbomb.com/lego-star-wars-the-force-awakens/3030-52537/")
		obj = obj.serialize_table()
		test = {"id": "52537","name": "LEGO Star Wars: The Force Awakens", "release_date": "2016-06-28 00:00:00", "aliases": None, "tiny_image": "http://www.giantbomb.com/api/image/square_mini/2822264-lswtfa.jpg", "num platforms": 12}

	def test_game_serialize_table_2(self):
		obj = Game("41088", "Pokémon X/Y", "2013-10-12 00:00:00", \
			"The first Pokémon games on the 3DS and the first to be released simultaneously worldwide.", \
			"http://www.giantbomb.com/api/image/square_mini/2482818-pokemonxy.jpg", "http://www.giantbomb.com/api/image/scale_medium/2482818-pokemonxy.jpg",\
			"PLATFORMS", "Pokemon X/Y\nPokemon Y", "http://www.giantbomb.com/pokemon-xy/3030-41088/")
		obj = obj.serialize_table()
		test = {"id": "41088","name": "Pokémon X/Y", "release_date": "2013-10-12 00:00:00", "aliases": "Pokemon X/Y\nPokemon Y", "tiny_image": "http://www.giantbomb.com/api/image/square_mini/2482818-pokemonxy.jpg", "num platforms": 2}

	def test_platform_serialize_table_1(self):
		obj = Platform("117", "Nintendo 3DS", "2011-02-26 00:00:00", "Nintendo", "249.00", "51630000", \
			"The Nintendo 3DS is a portable game console produced by Nintendo. The handheld features stereoscopic 3D technology that doesn't require glasses. It was released in Japan on February 26, 2011 and in North America on March 27, 2011.", \
			True, "3DS", "http://www.giantbomb.com/nintendo-3ds/3045-117/",\
			"http://www.giantbomb.com/api/image/square_mini/1686079-3dshw11911.jpg", "http://www.giantbomb.com/api/image/scale_medium/1686079-3dshw11911.jpg")
		obj = obj.serialize_table()
		test = {"id": "117", "name": "Nintendo 3DS", "release_date": "2011-02-26 00:00:00", "company": "Nintendo", "starting_price": "249.00", "tiny_image": "http://www.giantbomb.com/api/image/square_mini/1686079-3dshw11911.jpg"}
		self.assertEqual(obj, test)

	def test_platform_serialize_table_2(self):
		obj = Platform("20", "Xbox 360", "2005-11-22 00:00:00", "Microsoft Studios", "399.00", "80000000", \
			"The Xbox 360 is the second game console produced by Microsoft Corporation and is the successor to the original Xbox.", \
			True, "360\nXenon", "http://www.giantbomb.com/xbox-360/3045-20/",\
			"http://www.giantbomb.com/api/image/square_mini/195092-xbox_360_console_02.jpg", "http://www.giantbomb.com/api/image/scale_medium/195092-xbox_360_console_02.jpg")
		obj = obj.serialize_table()
		test = {"id": "20", "name": "Xbox 360", "release_date": "2005-11-22 00:00:00", "company": "Microsoft Studios", "starting_price": "399.00", "tiny_image": "http://www.giantbomb.com/api/image/square_mini/195092-xbox_360_console_02.jpg"}

	def test_character_serialize_table(self):
		obj = Character("5766", "Brock", None, "1", \
			"\"The Rock-Solid Pokémon Trainer!\"", \
			"DESCRIPTION", \
			"http://www.giantbomb.com/api/image/square_mini/1906766-pokemon_heartgold_soulsilver_brock.png", "http://www.giantbomb.com/api/image/scale_medium/1906766-pokemon_heartgold_soulsilver_brock.png", \
			"http://www.giantbomb.com/brock/3005-5766/", None, "3966")
		obj = obj.serialize_table()
		test = {"id": "5766", "gender": "1", "name": "Brock", "aliases": None, "first_appeared_in_game": "3966", "deck": "\"The Rock-Solid Pokémon Trainer!\"", "tiny_image": "http://www.giantbomb.com/api/image/square_mini/1906766-pokemon_heartgold_soulsilver_brock.png", "birthday": None}

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

"""
Name       Stmts   Miss Branch BrPart  Cover
--------------------------------------------
Tests.py     197     18     14      7    88%
"""

