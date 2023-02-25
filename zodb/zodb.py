import ZODB, ZODB.FileStorage
import transaction
import time
import logging
logging.basicConfig(filename='mysql.log', encoding='utf-8', level=logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')


# Create a new ZODB database and open a connection to it

storage = ZODB.FileStorage.FileStorage('objectdbFiles/mydata.fs')
db = ZODB.DB(storage)

start_time = time.time()
conn = db.open()
end_time = time.time()
print("Time to connect: " + str(end_time-start_time))
logging.info("Time to connect: " + str(end_time-start_time))

# Get the root object of the database
root = conn.root()

# Add some data to the database
root['Alex'] = {'Koblenz': 'Rauental'}
root['Ayush'] = 'Koblenz'

# Commit the transaction to the database
start_time = time.time()
transaction.commit()
end_time = time.time()
print("Time to insert records: " + str(end_time-start_time))
logging.info("Time to insert records: " + str(end_time-start_time))


# Query the database

start_time = time.time()

print(root['Alex'])
print(root['Ayush'])

end_time = time.time()
print("Time to retrieve records: " + str(end_time-start_time))
logging.info("Time to retrieve records: " + str(end_time-start_time))

# Close the connection to the database
conn.close()
db.close()