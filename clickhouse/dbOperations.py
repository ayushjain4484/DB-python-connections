import clickhouse_connect
import time
import logging
logging.basicConfig(filename='clickhouse.log', encoding='utf-8', level=logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
start_time = time.time()

#https://clickhouse.com/docs/en/integrations/language-clients/python/intro/

client = clickhouse_connect.get_client(host='localhost', username='default', password='')

end_time = time.time()
print("Time to connect: " + str(end_time-start_time))
logging.info("Time to connect: " + str(end_time-start_time))
#client.command('CREATE TABLE new_table (key UInt32, value String, metric Float64) ENGINE MergeTree ORDER BY key')

row1 = [1000, 'String Value 1000', 5.233]
row2 = [2000, 'String Value 2000', -107.04]
data = [row1, row2]

start_time = time.time()

client.insert('new_table', data, column_names=['key', 'value', 'metric']) 

end_time = time.time()
print("Time to insert data: " + str(end_time-start_time))
logging.info("Time to insert data: "+ str(end_time-start_time))

start_time = time.time()

result = client.query('SELECT max(key), avg(metric) FROM new_table')

end_time = time.time()
print("Time to retrieve data: " + str(end_time-start_time))
logging.info("Time to retrieve data: "+ str(end_time-start_time))

print(result.result_rows)