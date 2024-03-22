from swapi_test import *
from swapi_oop import *

class1 = Starwars()
class1.db.create_collection("starships")
class1.get_pilots_id()

class1.mongo_insert()

if __name__ == "__main__":
    unittest.main()