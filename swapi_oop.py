import requests
import pymongo


class Starwars:
    url_starship = "https://swapi.dev/api/starships"

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['starwars']
        self.starships = None
        try:
            self.response = requests.get(self.url_starship)
            self.starships = self.response.json()
        except:
            print("invalid requests")

    def get_pilots(self, pilot_url):
        try:
            if pilot_url:
                pilot_response = requests.get(pilot_url)
                pilot_results = pilot_response.json()
                return pilot_results
        except:
            print("pilots don't exists!")

    def get_pilots_id(self):
        for ship in self.starships["results"]:
            updated_pilots = []
            for pilot in ship["pilots"]:
                star_name = self.get_pilots(pilot)["name"]
                star_id = self.db.characters.find_one({"name": star_name}, {"_id": 1})
                pilot = star_id["_id"]
                updated_pilots.append(pilot)
            ship["pilots"] = updated_pilots




        # import pymongo
        # from swapi import *
        # client = pymongo.MongoClient()
        #
        # db = client["starwars"]
        #
        # for ship in starships["results"]:
        #     updated_pilots = []
        #     for pilot in ship["pilots"]:
        #         star_name = get_pilots(pilot)["name"]
        #         star_id = db.characters.find_one({"name": star_name}, {"_id": 1})
        #         pilot = star_id["_id"]
        #         updated_pilots.append(pilot)
        #     ship["pilots"] = updated_pilots

class1 = Starwars()
class1.get_pilots_id()
print(class1.starships)