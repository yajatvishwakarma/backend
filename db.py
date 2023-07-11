from pymongo import MongoClient


def get_database_connection():
    client = MongoClient(
        "mongodb+srv://yajat:yajat123@judgy.bwe2k0q.mongodb.net/?retryWrites=true&w=majority")
    return client["mydatabase"]
