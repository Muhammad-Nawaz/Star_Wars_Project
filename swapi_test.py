import unittest
from swapi_oop import *
from bson import ObjectId


class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sw1 = Starwars()
        self.sw2 = Starwars()
        self.sw3 = Starwars()

    def test_get_ship(self):
        actual = self.sw1.get_pilots("https://swapi.dev/api/starships/10/")["name"]
        expected = "Millennium Falcon"
        self.assertEqual(
            actual, expected,
            "Expected `get_pilots` method to fetch ship's name."
        )

    def test_get_pilots_names(self):
        actual = self.sw2.get_pilots("https://swapi.dev/api/starships/10/")["pilots"]
        expected = [
            "https://swapi.dev/api/people/13/",
            "https://swapi.dev/api/people/14/",
            "https://swapi.dev/api/people/25/",
            "https://swapi.dev/api/people/31/"
        ]
        self.assertEqual(
            actual, expected,
            "Expected `get_pilots` method to fetch pilot's name."
        )

    def test_get_no_pilots_names(self):
        actual = self.sw3.get_pilots("https://swapi.dev/api/starships/9/")["pilots"]
        expected = []
        self.assertEqual(
            actual, expected,
            "Expected `get_pilots` method to return no name."
        )

    # to be continued
    def test_get_non_existent_starship(self):
        actual = self.sw3.get_pilots("https://swapi.dev/api/starships/1/")
        expected = {'detail': 'Not found'}
        self.assertEqual(
            actual, expected,
            "Expected `get_pilots` method to return error."
        )

    def test_get_pilots_id(self):
        # pilots = self.sw3.get_pilots_id("https://swapi.dev/api/starships/12/")["pilots"]
        self.sw3.get_pilots_id()
        actual = self.sw3.star_id

        expected = [
            {'_id': ObjectId('65f9a9a044466c62a7acc2cb')}, {'_id': ObjectId('65f9a9abad2e4088d35107a6')},
            {'_id': ObjectId('65f9a9b105c39e25f3d08ea3')}, {'_id': ObjectId('65f9a9b7692015794871c95b')},
            {'_id': ObjectId('65f9a9b3fcaf6bcd19c12cfa')}, {'_id': ObjectId('65f9a99d645177e9dc10318f')},
            {'_id': ObjectId('65f9a9cbdd190ab346f4d457')}, {'_id': ObjectId('65f9a9ae2487cf43b558ddf5')},
            {'_id': ObjectId('65f9a9a3352619b612f57573')}
        ]
        self.assertEqual(
            actual, expected,
            "Expected `get_pilots` method to return error."
        )

        def test_insert_mongo(self):
            actual = self.sw3.db.starships.find({"name": "X-wing"}).next()

            expected = {'_id': ObjectId('65fc1dce1f4b37bf8f188fa9'), 'name': 'X-wing', 'model': 'T-65 X-wing',
                        'manufacturer': 'Incom Corporation', 'cost_in_credits': '149999', 'length': '12.5',
                        'max_atmosphering_speed': '1050', 'crew': '1', 'passengers': '0', 'cargo_capacity': '110',
                        'consumables': '1 week', 'hyperdrive_rating': '1.0', 'MGLT': '100',
                        'starship_class': 'Starfighter',
                        'pilots': [ObjectId('65f9a9b3fcaf6bcd19c12cfa'), ObjectId('65f9a99d645177e9dc10318f'),
                                   ObjectId('65f9a9cbdd190ab346f4d457'), ObjectId('65f9a9ae2487cf43b558ddf5')],
                        'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                                  'https://swapi.dev/api/films/3/'], 'created': '2014-12-12T11:19:05.340000Z',
                        'edited': '2014-12-20T21:23:49.886000Z', 'url': 'https://swapi.dev/api/starships/12/'}

            self.assertEqual(
                actual, expected,
                "Expected `insert_mongo` method to insert starships data into collection."
            )


if __name__ == "__main__":
    unittest.main()
