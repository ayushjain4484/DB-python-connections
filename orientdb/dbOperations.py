import pyorient

user = "root"
password = "root"
#dbName = "testDB"
dbName = "testDB_graph"


# Connect to the OrientDB server
client = pyorient.OrientDB("localhost", 2424)

# Enable Token-based Authentication
client.set_session_token(True)

# Getting session ID
session_id = client.connect(user, password)

# TO CREATE DATABASE
"""
# Dropping DB if it already exists
client.db_drop(dbName)

# Create the database
client.db_create(
       dbName,
       pyorient.DB_TYPE_GRAPH,
       pyorient.STORAGE_TYPE_PLOCAL)
"""

# Open the database

if not client.db_exists(dbName):
    client.db_open(dbName,user,password)

data = {
  "@Person": {
      "Name": "ayush"
   }
}

client.record_create(1, data)

# Disconnect from the OrientDB server
client.disconnect("Disconnected")