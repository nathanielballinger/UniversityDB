from io             import StringIO
from unittest       import main, TestCase
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
		platform1 = Platform("117", "Nintendo 3DS", "02/26/2011", "Nintendo", "$249", "59790000", \
			"Nintendo announced the Nintendo 3DS on March 23, 2010. No software was yet revealed; the only details in the announcement were that the system will be available in Japan by the end of March 2011, and that it will display stereoscopic 3D without requiring special glasses, and it is backwards compatible with existing DS and DSi software. The system itself was revealed at Nintendo's E3 2010 media briefing by Satoru Iwata.", \
			"SUPPORT", "3DS", "URL", "IMAGE")

		self.assertEqual(platform1.id, "117")
		self.assertEqual(platform1.name, "Nintendo 3DS")
		self.assertEqual(platform1.release_date, "02/26/2011")

	def test_case_platform_2(self):
		platform2 = Platform("20", "Xbox 360", "11/22/2005", "Microsoft", "$399", "80000000", \
			"Co-Developed with IBM, ATI, and Silicon Integrated Systems, the Xbox 360 uses the triple-core IBM designed Xenon as its CPU, ATI Xenos which has 10 MB of embedded eDRAM as the graphics processor and has a main memory pool of 512 MB. Development of the Xbox 360 began in early 2003, a year and a half after the original Xbox release.", \
			"SUPPORT", "X360", "URL", "IMAGE")

		self.assertEqual(platform2.id, "20")
		self.assertEqual(platform2.abbrevations, "X360")
		self.assertEqual(platform2.starting_price, "$399")

	def test_case_platform_3(self):
		platform3 = Platform("35", "PlayStation 3", "11/11/2006", "Sony", "$599", "80000000", \
			"The PS3 uses the Cell Broadband Engine co-developed by Sony, IBM, and Toshiba. Graphics processing is handled by the NVIDIA RSX 'Reality Synthesizer', which can output resolutions up to 1080p HD. The PS3 has 256 MB of XDR main memory and 256 MB of GDDR3 video memory for the RSX, for a total of 512 MB system memory.", \
			"SUPPORT", "PS3", "URL", "IMAGE")

		self.assertEqual(platform3.id, "35")
		self.assertEqual(platform3.number_units_sold, "80000000")
		self.assertEqual(platform3.company, "Sony")

	def test_case_platform_4(self):
		platform4 = Platform("146", "PlayStation4", "11/15/2013", "Sony", "$399", "40000000", \
			"The PlayStation 4 is the fourth video game console produced by the Sony Corporation, and was released November 15th in North America and November 29th in Europe and Australia. It uses the x86 processor and 8GB of GDDR5 memory, making it much more PC-like (and easier to code for) than Sony's previous console, the PlayStation 3.", \
			"SUPPORT", "PS4", "URL", "IMAGE")

		self.assertEqual(platform4.id, "146")
		self.assertEqual(platform4.starting_price, "$399")
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
		character1 = Character("1", "Sub-Zero", "Male", "DECK", "Mortal Kombat", \
			"Sub-Zero is a video game character from the Mortal Kombat series and one of the original characters in the first Mortal Kombat game in 1992. A mainstay of the series, Sub-Zero is the only character who has appeared in every main Mortal Kombat fighting game. The character also appears in many other Mortal Kombat media works such as the Mortal Kombat live action film series and animated series.", \
			"IMAGE", "URL", "None","None")

		self.assertEqual(character1.id, "1")
		self.assertEqual(character1.name, "Sub-Zero")
		self.assertEqual(character1.gender, "Male")

	def test_case_character_2(self):
		character2 = Character("2", "Mario", "Male", "DECK", "Donkey Kong", \
			"Mario is a fictional character in the Mario video game franchise, owned by Nintendo and created by video game designer Shigeru Miyamoto. Serving as the company's mascot and the eponymous protagonist of the series, Mario has appeared in over 200 video games since his creation. Depicted as a short, pudgy, Italian plumber who resides in the Mushroom Kingdom, his adventures generally center upon rescuing Princess Peach from the Koopa villain Bowser. His younger brother is Luigi.", \
			"IMAGE", "URL", "None","None")

		self.assertEqual(character2.id, "2")
		self.assertEqual(character2.game_first_appeared, "Donkey Kong")
		self.assertEqual(character2.gender, "Male")

	def test_case_character_3(self):
		character3 = Character("3", "Brock", "Male", "DECK", "Pokémon Red and Blue", \
			"Brock is a fictional character in the Pokémon franchise owned by Nintendo. In the Pokémon video games, he is the Gym Leader of Pewter City and mainly uses Rock-type Pokémon. In the anime series, Ash comes across a man that is later revealed to be Brock's father. He explains that Brock wanted to become a Pokémon Master but due to his father leaving, Brock had to take care of his many, many siblings and could not leave. This is why he became a gym leader, to stay close to his family. His father comes back and states he will take care of the family. Brock left his position as a Gym Leader to travel alongside Ash Ketchum and became a revered Pokémon Breeder. He later cultivates his skill in medicine. As of the latest Japanese episode, Brock is at Pewter City to train to be a Pokémon Doctor.", \
			"IMAGE", "URL", "None","None")

		self.assertEqual(character3.id, "3")
		self.assertEqual(character3.name, "Brock")
		self.assertEqual(character3.game_first_appeared, "Pokémon Red and Blue")

	def test_case_character_4(self):
		character4 = Character(" "," "," "," "," "," "," "," "," "," ")
		
		self.assertEqual(character4.id, " ")
		self.assertEqual(character4.name, " ")
		self.assertEqual(character4.game_first_appeared, " ")

# ----
# Main
# ----

if __name__ == '__main__' :
	main()

