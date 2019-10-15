import pymongo

DB_NAME = 'N-OJ'

USER_DOC = 'user'

MONGO_CLIENT = pymongo.MongoClient('mongodb://localhost:27017/')
OJ_DB = MONGO_CLIENT[DB_NAME]
