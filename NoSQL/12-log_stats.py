#!/usr/bin/env python3
"""
<<<<<<< HEAD
Nginx logs stats from MongoDB
=======
Nginx logs stats from MongoDB.
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
"""

from pymongo import MongoClient

<<<<<<< HEAD

def main():
    """Provides stats about Nginx logs stored in MongoDB."""
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
=======
if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")  # <-- 4 spaces (IMPORTANT)

    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print(f"{status_check} status check")
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
