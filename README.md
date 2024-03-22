# Star_Wars_Project

![image](https://github.com/Muhammad-Nawaz/Star_Wars_Project/assets/65783110/aa2f384a-ef57-4cf0-87d1-11faeed62320)


## Table of Contents
- [Introduction](###Introduction)
- [How to run the project](###Howtoruntheproject)
- [Documents](###Documents)
- [Unit Testing](###UnitTesting)
- [Definition of Done](###DefinitionOfDone)
- [Team Compliance Of Agile & SCRUM](###Agile&Scrum)
- [Improvements](#Improvements)


### Introduction


The project objective is to extract starship data from the Star Wars API website (https://swapi.dev/) and import them into an existing MongoDb Database. The 'pilots' key from the starships' data, which comprises URLs pointing to the characters who pilot these vessels will also be extracted. We'll then seamlessly replace these URLs with a curated list of ObjectIDs retrieved from the characters collection within our MongoDB database. This enables us to conveniently access the pilots' ObjectID list directly from the MongoDB page. To ensure precision and reliability, we've implemented thorough unit tests to validate each step of the process, guaranteeing seamless execution without errors.


### How to run the project
 
The prerequisite libraries needed for the project are pymongo and requests. To run the project, we Git cloned our respository onto our local machines, and performed Git Pull to get the latest version of the project and to run the main.py file. We decided to produce this code in an OOP format, so the code would be well organized and link seamlessly with the Test coding. To run this program, we used the URL from the Star Wars website "swapi" to attain the data for the Starships and set this under the 'class' Starwars. We initialised this and wrote code to store the information in JSON format. The program then iterates through the information and then inserts each document into the MongoDB database.


### Documents: 

swapi_oop.py - Main file including the classes that will fetch starship data and update the MongoDB collection. 

swapi_test.py - Implementations of unit testing.

main.py - The main file to initiate the swapi_oop.py file




### Unit Testing:
The team collaboratively designed unit tests to ensure the functionality of the code that will be used for the final file. The tests included:

1. test_get_ship
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 10. 
The expected output is identified through looking at the starship name online e.g. "Millenium Falcon".

![image](https://github.com/Muhammad-Nawaz/Star_Wars_Project/assets/65783110/95fc4069-3959-4099-8f38-0740e11f6fae)


2. A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 10, to fetch their corresponding pilot urls.
The expected output is 4 pilot urls. 

![image](https://github.com/Muhammad-Nawaz/Star_Wars_Project/assets/65783110/e42d6beb-e527-4b4f-90e0-022218a75677)




3. test_get_pilots_names
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 10, to fetch their corresponding pilot urls.
The expected output are 4 pilot urls. 


4. test_get_no_pilots_names
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 9 and searches for the pilot url(s), which has no records.
The expected output is an empty list. 



5. test_get_non_existent_starship
A test that uses the get_pilots method (from the swapi_oop.py file) passing in the API address for starship 1, which has no record.
The expected output is a library {'detail': 'Not found'}. 



6. test_get_pilots_id
A test that uses the get_pilots_id() method (from the swapi_oop.py file) passing in the API address for starship 12 and returns the ids for each of the coreesponding pilots.
The expected output is are the ObjectIds in the format {'_id': ObjectId('65f9a9a044466c62a7acc2cb')}.







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




### Definition of Done:
 
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
User Story 1: We were able to secure an API connection to retrieve the star wars starships information through unit testing 1 - test_get_ship.

User story 2: We were able to update the MongoDB database with current starship information through the unit testing 6 - test_insert_mongo.

User story 3: We were able to view the full list of starship data using unit testing 1 - test_get_ship.

User story 6: We were able to search for the pilot(s) name(s) that are associated with a certain starship through the unit testing 2 - test_get_pilots_names.

User story 7: We were able to get a response where there are empty fields through using unit testing 3 - test_get_no_pilots_names.


Team Compliance Of Agile & SCRUM
- Use of a Kanban board with Trello (a tool used to manage the scrum framework): https://trello.com/b/4j8cJPBL/star-wars
- Scrum meetings and 3 sprints
- Updated the product backlog
- Created user stories on Trello and updated them with definition of done
- Sprint retrospective and a post metro retro (a tool for the agile framework to see what went well and what to improve on): https://metroretro.io/BOP1GIWEYZXF




### Improvements:
1. Testing: Expand test coverage by writing additional unit tests to validate the behavior of the Starwars class under various scenarios. Consider implementing automated testing to catch regressions and ensure reliability.
2. Practice: Need more practice for unittest.
3. Add in the additional functionality of User stories 4,5 & 8 (these were non-essential).
4.  Refactoring: Regularly review the codebase to identify areas for improvement, such as simplifying complex functions, removing duplicated code, or optimizing performance.



