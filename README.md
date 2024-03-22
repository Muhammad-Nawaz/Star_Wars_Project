# Star_Wars_Project

A Sparta Global Data Engineering 401 mini project to pull data on all available starships from an online API. The "pilots" key contains URLs pointing to the characters who pilot the starship. This will be used to replace 'pilots' with a list of ObjectIDs from the characters collection in previously used MongoDB database, then the starships will be inserted into their own collection.

## Table of Contents
- [Documents](###Documents)
- [Unit Testing](###UnitTesting)
- [Contributing](#contributing)
- [License](#license)





### Documents: 

swapi_oop.py - Main file including the classes that will fetch starship data and update the MongoDB collection. 

swapi_test.py - Implementations of unit testing.





### Unit Testing:
The team collaboratively designed unit tests to ensure the functionality of the code that will be used for the final file. The tests included:

1. test_get_ship
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 10. 
The expected output is identified through looking at the starship name online e.g. "Millenium Falcon".


2. test_get_pilots_names
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 10, to fetch their corresponding pilot urls.
The expected output are 4 pilot urls. 


3. test_get_no_pilots_names
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 9 and searches for the pilot url(s), which has no records.
The expected output is an empty list. 



4. test_get_non_existent_starship
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 1, which has no record.
The expected output is a library {'detail': 'Not found'}. 



5. test_get_pilots_id
A test that uses the get_pilots_id() method (from the swapi_oop.py file) passing in the API address for starship 12 and returns the ids for each of the coreesponding pilots.
The expected output is are the ObjectIds in the format {'_id': ObjectId('65f9a9a044466c62a7acc2cb')}.



6. test_insert_mongo
A test that searches for the information of a starhip to confirm that the starship information has been imported into the mongodb datase. In this example, ("X-wing") is used. 
The expected output is a library with the corresponding "X-wing" information.



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




### Definitaion of Done:
 
Project:
Our project objective is to establish a connection to the Starwars API for accessing information about starships. Specifically, we aim to retrieve pilot IDs based on the starship name using MongoDB.

Sprints:
First Sprint:
Roles were divided, and a Kanban board was set up.
User stories were created.

Second Sprint:
The scrum master initialized the repository, and collaborative coding commenced.
A README file was added to document project details.
Third Sprint:
Following communication with the client, a more detailed project plan was established.
Objectives were outlined in the README, and preparations for the project presentation began.

User stories:
(The user stories can be found on our Kanban board on Trello here: https://trello.com/b/4j8cJPBL/star-wars)
User Story 1: We were able to secure an API connection to retrieve the star wars starships information through unit testing 1, test_get_ship.

User story 2: We were able to update the MongoDB database with current starship information through the unit testing 6, test_insert_mongo.

User story 3: We were able to view the full list of starship data 

User story 6: We were able to search for the pilot(s) name(s) that are associated with a certain starship through the unit testing 2, test_get_pilots_names.

User story 7: We were able to get a response where there are empty fields through using unit testing 3, test_get_no_pilots_names.
 

### Improvement:
1. Testing: Expand test coverage by writing additional unit tests to validate the behavior of the Starwars class under various scenarios. Consider implementing automated testing to catch regressions and ensure reliability.
2. Practice: Need more practice for unittest.
3.  Refactoring: Regularly review the codebase to identify areas for improvement, such as simplifying complex functions, removing duplicated code, or optimizing performance.



