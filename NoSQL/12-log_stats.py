#!/usr/bin/env python3
"""
Nginx logs stats from MongoDB.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")

    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print(f"{status_check} status check")