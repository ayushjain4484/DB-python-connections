import time
import logging
start_time = time.time()
from pymongo import MongoClient
logging.basicConfig(filename='mongo-db.log', encoding='utf-8', level=logging.DEBUG)

def get_database():
   client = MongoClient("mongodb://172.17.0.2")
   return client
  
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
   # Get the database
   dbclient = get_database()
   
   if dbclient:
    print("connected")
    logging.info("connected to DB")
    logging.info("time taken for connection : "+str(time.time()-start_time)+" seconds")
    dbclient.close()