from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
def get_db_handle(pms_database, host, port, username, password):

 client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['pms_databse']
 return db_handle, client
