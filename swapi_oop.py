import requests
import pymongo


class Starwars:
    url_starship = "https://swapi.dev/api/starships"

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['starwars']
        self.starships = None
        self.star_id = None
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
            return "no pilot_url provided"
        except:
            # print("pilots/ships don't exists!")
            raise Exception("pilots/ships don't exists!")

    def get_pilots_id(self):
        id_strings = []
        for ship in self.starships["results"]:
            updated_pilots = []
            for pilot in ship["pilots"]:
                star_name = self.get_pilots(pilot)["name"]
                star_id = self.db.characters.find_one({"name": star_name}, {"_id": 1})
                pilot = star_id["_id"]
                updated_pilots.append(pilot)
                id_strings.append(star_id)
            ship["pilots"] = updated_pilots
        self.star_id = id_strings

    def mongo_insert(self):
        for ship in self.starships["results"]:
            self.db.starships.insert_one(ship)
        print("Successfully inserted data into starships collection.")


