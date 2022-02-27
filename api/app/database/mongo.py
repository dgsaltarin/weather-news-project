# python
from os import environ
# mongoDB
from pymongo import MongoClient

## Connection to mongoDB

def connection():

    user = environ['mongodb_user'] or 'admin'
    secret = environ['mongodb_secret'] or 'wfg0wpMfEpRm6Co6'
    host = environ['mongodb_host'] or 'cluster0.sgaqs.mongodb.net/userSession'

    #client = MongoClient("mongodb+srv://admin:adminCMS@cluster0.xoky5.mongodb.net/users-db?retryWrites=true&w=majority")
    client = MongoClient(f"mongodb+srv://{user}:{secret}@{host}")
    
    return client


def dataBase():
    return connection().userSession


def collection():
    return dataBase().searchHistory

