#!/usr/bin/env python3
""" 12. Log stats """
from pymongo import MongoClient


client = MongoClient('mongodb://172.17.0.2:27017')
collection = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """ provides some stats about Nginx logs stored in MongoDB """
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, mongo_collection.count_documents({"method": method})))

    print("{} status check".format(mongo_collection.count_documents({"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    log_stats(collection)
