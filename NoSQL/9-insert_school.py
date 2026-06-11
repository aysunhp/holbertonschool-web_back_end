#!/usr/bin/env python3
""" Insert document """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Insert a school with features

        Args:
            mongo_collection: Collection to pass
            kwargs: Dictionary with elements to put

        Return:
            Id of the new element
    """
    new_school = mongo_collection.insert_one(kwargs)

<<<<<<< HEAD
    return (new_school.inserted_id)
=======
    return (new_school.inserted_id)
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
