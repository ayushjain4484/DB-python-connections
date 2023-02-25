from neo4j import GraphDatabase
import time
import logging
logging.basicConfig(filename='mysql.log', encoding='utf-8', level=logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')


# Connect to the Neo4j database

start_time = time.time()
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
end_time = time.time()
print("Time to connect: " + str(end_time-start_time))
logging.info("Time to connect: " + str(end_time-start_time))


if driver:
    print("Connection to GraphDB instance in Docker container established")
else:
    print("Connection to GraphDB instance in Docker container failed")


# Define some data to insert
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

# Insert the data into the database
start_time = time.time()
with driver.session() as session:
    for record in data:
        session.run("CREATE (:Person {name: $name, age: $age})", **record)
end_time = time.time()
print("Time to insert records: " + str(end_time-start_time))
logging.info("Time to insert records: " + str(end_time-start_time))

# Retrieve the data from the database
start_time = time.time()
with driver.session() as session:
    result = session.run("MATCH (p:Person) RETURN p.name, p.age")

    # Print the data
    for record in result:
        print(f"{record['p.name']} is {record['p.age']} years old")

end_time = time.time()
print("Time to retrieve records: " + str(end_time-start_time))
logging.info("Time to retrieve records: " + str(end_time-start_time))

driver.close()