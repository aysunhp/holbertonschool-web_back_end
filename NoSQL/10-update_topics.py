#!/usr/bin/env python3
""" Update School """
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    """ Change the data
    
        Args:
            mongo_collection:
            name: School
            topics: School name

        Return:
            Nothing
    """
    query: dict = {'name': name}
<<<<<<< HEAD
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
=======
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
