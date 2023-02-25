import pymysql
import pymysql.cursors
import time
import logging
logging.basicConfig(filename='mysql.log', encoding='utf-8', level=logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
start_time = time.time()

# Connect to the database
connection = pymysql.connect(host='172.17.0.2',
                             user='root',
                             password='secret',
                             database='mysql',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

if connection:
    print("connected")
    logging.info("connected to DB")
    logging.info("time taken for connection : "+str(time.time()-start_time)+" seconds")

cursor = connection.cursor()


SQL = "select user from user;" 
logging.info("SQL: "+SQL)
time_before_sql = time.time()
cursor.execute(SQL)
logging.info("time taken to execute SQL : "+str(time.time() - time_before_sql)+ " seconds" )
result = cursor.fetchall()
  
# loop through the rows
for row in result:
     print(row)
     print("\n")

print("--- program execution time: %s seconds ---" % (time.time() - start_time))