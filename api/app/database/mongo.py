# python
from os import environ
# mongoDB
from pymongo import MongoClient

## Connection to mongoDB

def connection():

    user = environ['mongodb_user']
    secret = environ['mongodb_secret']
    host = environ['mongodb_host']

    client = MongoClient(f"mongodb+srv://{user}:{secret}@{host}")
    
    return client


def dataBase():
    return connection().userSession


def collection():
    return dataBase().searchHistory

