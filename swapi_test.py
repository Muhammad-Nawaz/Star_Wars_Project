import unittest
from swapi_oop import *

class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sw1 = Starwars()
        self.sw2 = Starwars()
        self.sw3 = Starwars()

    def test_get_pilots(self):
        actual = self.sw1.get_pilots("https://swapi.dev/api/starships/10/")["name"]
        expected = "Millennium Falcon"
        self.assertEqual(
                    actual, expected,
                    "Expected `get_pilots` method to fetch ship's name."
        )
        # def get_pilots(self, pilot_url):
        #     try:
        #         if pilot_url:
        #             pilot_response = requests.get(pilot_url)
        #             pilot_results = pilot_response.json()
        #             return pilot_results
        #     except:
        #         print("pilots don't exists!")




        # def test_order(self):
        #     self.table02.order('Food', 10.00, 3)
        #     actual = self.table02.bill
        #     expected = [{
        #         'item': 'Food',
        #         'price': 10.00,
        #         'quantity': 3}]
        #     self.assertEqual(
        #         actual, expected,
        #         "Expected `order` method to create object in bill instance variable."
if __name__ == "__main__":
    unittest.main()