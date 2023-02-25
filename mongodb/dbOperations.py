from pprint import pprint

from pymongo import MongoClient
import urllib.parse
import time
import logging
logging.basicConfig(filename='mongo.log', encoding='utf-8', level=logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
start_time = time.time()

client = MongoClient("mongodb://127.0.0.1")
current_time = time.time()

#logging the time
print("Time taken to connect: " + str(current_time-start_time))
logging.info("Time taken to connect: " + str(current_time-start_time))

print("Connection Successful")

mydb = client["mydatabase"]

print(client.list_database_names())


 #Creating a collection
coll = mydb['students']
coll.drop()
# #Inserting document into a collection
data = [
   {"_id": "1001", "name": "Ram", "age": "26", "city": "Hyderabad"},
   {"_id": "1002", "name": "Rahim", "age": "27", "city": "Bangalore"},
   {"_id": "1003", "name": "Robert", "age": "28", "city": "Mumbai"},
   {"_id": "1004", "name": "Romeo", "age": "25", "city": "Pune"},
   {"_id": "1005", "name": "Sarmista", "age": "23", "city": "Delhi"},
   {"_id": "1006", "name": "Rasajna", "age": "26", "city": "Chennai"}
]
start_time = time.time()

res = coll.insert_many(data)
end_time = time.time()

print("Time taken to insert into database: " + str(end_time - start_time))
logging.info("Time taken to insert into database: " + str(end_time - start_time))
print("Data inserted ......")

# #Retrieving data
print("Documents in the collection: ")

start_time = time.time()
for doc1 in coll.find({"name":"Sarmista"}):
    print(doc1)
end_time = time.time()

print("Time taken to retrieve from database: " + str(end_time - start_time))
logging.info("Time taken to retrieve from database: " + str(end_time - start_time))

client.close()