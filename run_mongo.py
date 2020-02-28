import pymongo
from app_logs.app_logger import Logger

MONGO_URI = "mongodb://radmin:radmin@127.0.0.1:27017"
logger = Logger().get()

class MongoAdapter():
    #

    def __init__(self):
        self.client = None
        self.database = None
        self.connection_status = False

    def connect_mongodb(self):
        try:
            self.client = pymongo.MongoClient(MONGO_URI)
            self.connection_status = True
        except pymongo.errors.ServerSelectionTimeoutError as ex:
            logger.error(ex)
        except pymongo.errors.ConnectionFailure as ex:
            logger.error(ex)
        except Exception as ex:
            logger.error(ex)
        return self.client

    def get_mongo_database(self, selected_db="test"):
        self.database = self.client[selected_db]
        return self.database

    def close_mongo_database(self):
        print("Closing ...")
        self.client.close()

    def insert_mongo(self):
        pass
    def update_mongo(self):
        pass
    def get_mongo(self):
        pass
    def delete_mongo(self):
        pass


if __name__ == "__main__":

    try:
        logger.info("Mongo started")
        print("#################")
        print("https://www.w3schools.com/python/python_mongodb_create_collection.asp")
        print("https://docs.mongodb.com/manual/reference/mongo-shell/")
        print("https://docs.mongodb.com/manual/core/databases-and-collections/")
        print("#################")
        print("In MongoDB, databases hold collections of documents.")
        mg = MongoAdapter()
        mg.connect_mongodb()
        print("client: " + str(mg.client))
        print("database: " + str(mg.client.db))
        mydb = mg.get_mongo_database()
        print("selected dbs\n " + str(mydb))
        mycol = mydb["users"]
        print(mycol.insert_one({"name": "12"}))
        rv = mydb.list_collection_names()
        print(rv)
        po = mycol.insert_one({"name": "esp"}).inserted_id
        print("inserted: " + str(po))
        for d in mycol.find():
            print(d)
        mycol.drop()
        mg.close_mongo_database()
    except KeyboardInterrupt as ex:
        print(ex)
        print("closing")
