# Star_Wars_Project

A Sparta Global Data Engineering 401 mini project to pull data on all available starships from an online API. The "pilots" key contains URLs pointing to the characters who pilot the starship. This will be used to replace 'pilots' with a list of ObjectIDs from the characters collection in previously used MongoDB database, then the starships will be inserted into their own collection.


### Documents: 

swapi_oop.py - Main file including the classes that will fetch starship data and update the MongoDB collection. 

swapi_test.py - Implementations of unit testing.





### Unit Testing:
The team collaboratively designed unit tests to ensure the functionality of the code that will be used for the final file. The tests included:

test_get_pilots

test_get_no_pilots_names

test_get_non_existent_starship

test_get_pilots_id


### swapi_oop.py:
The Starwars class is designed to interact with the Star Wars API (swapi.dev) and a MongoDB database to fetch starship data and store it in the database. The functions include:

1. __init__(self)
This is the constructor method for the Starwars class. It creates a connection to a MongoDB database named 'starwars' using the pymongo.MongoClient() constructor. It also sends a GET request to the Star Wars API endpoint (https://swapi.dev/api/starships) to fetch information about starships. 

2. get_pilots(self, pilot_url)
This method retrieves information about pilots associated with a given starship. It takes a pilot_url parameter, which is the URL to the pilot's information in the Star Wars API.


3. get_pilots_id(self)
This method iterates over the starships fetched from the Star Wars API and retrieves the MongoDB _id for each pilot associated with a starship.

4. mongo_insert(self)
This method inserts the starship data fetched from the Star Wars API into the MongoDB database.    