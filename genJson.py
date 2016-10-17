import json
import urllib.request


api_key="d0d1072f35f6c08b0ce0d7249c1c1d94d500c913"
gameFieldList = "&field_list=id,name,original_release_date,genres,developers,original_rating,description,review,image,platforms,characters,aliases,site_detail_url"
game1URL = "http://www.giantbomb.com/api/game/1/?api_key="+api_key+"&format=json"+gameFieldList
game2URL = "http://www.giantbomb.com/api/game/2/?api_key="+api_key+"&format=json"+gameFieldList
game3URL = "http://www.giantbomb.com/api/game/3/?api_key="+api_key+"&format=json"+gameFieldList
platformFieldList ="&field_list=id,name,abbreviation,company,deck,description,image,install_base,online_support,original_price,release_date,site_detail_url"
platform1URL = "http://www.giantbomb.com/api/platform/1/?api_key="+api_key+"&format=json"+platformFieldList
platform1URL = "http://www.giantbomb.com/api/platform/2/?api_key="+api_key+"&format=json"+platformFieldList
platform1URL = "http://www.giantbomb.com/api/platform/3/?api_key="+api_key+"&format=json"+platformFieldList
characterFieldList = "&field_list=id,aliases,birthday,deck,description,enemies,friends,first_appeared_in_game,games,gender,image,name,site_detail_url"
character1URL = "http://www.giantbomb.com/api/character/1/?api_key="+api_key+"&format=json"+characterFieldList
character2URL = "http://www.giantbomb.com/api/character/2/?api_key="+api_key+"&format=json"+characterFieldList
character3URL = "http://www.giantbomb.com/api/character/3/?api_key="+api_key+"&format=json"+characterFieldList

if __name__ == "__main__":
	pass



