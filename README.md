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
