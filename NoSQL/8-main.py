#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
<<<<<<< HEAD
        print("[{}] {}".format(school.get('_id'), school.get('name')))
=======
        print("[{}] {}".format(school.get('_id'), school.get('name')))
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
