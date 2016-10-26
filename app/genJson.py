import json
import urllib.request


api_key="d0d1072f35f6c08b0ce0d7249c1c1d94d500c913"
gameFieldList = "&field_list=id,name,original_release_date,genres,developers,original_rating,description,review,image,platforms,characters,aliases,site_detail_url"
platformFieldList ="&field_list=id,name,abbreviation,company,deck,description,image,install_base,online_support,original_price,release_date,site_detail_url"
characterFieldList = "&field_list=id,aliases,birthday,deck,description,enemies,friends,first_appeared_in_game,games,gender,image,name,site_detail_url"

games = []
for x in range(0,520):
	gameString = "http://www.giantbomb.com/api/games/?api_key="+api_key+"&format=json"+gameFieldList+"&offset"+str(x)+"00"
	games.append(gameString)

platforms = []
for x in range(0,2):
	platformString = "http://www.giantbomb.com/api/platforms/?api_key="+api_key+"&format=json"+gameFieldList+"&offset"+str(x)+"00"
	platforms.append(platformString)

characters = []
for x in range(0,332):
	characterString = "http://www.giantbomb.com/api/characters/?api_key="+api_key+"&format=json"+gameFieldList+"&offset"+str(x)+"00"
	characters.append(characterString)

if __name__ == "__main__":
	print(platform1URL)
	print(platform2URL)
	print(platform3URL)
	print(character1URL)
	print(character2URL)
	print(character3URL)



