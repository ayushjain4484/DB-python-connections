from neo4j import GraphDatabase

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

if driver:
    print("Connection to GraphDB instance in Docker container established")
else:
    print("Connection to GraphDB instance in Docker container failed")

driver.close()