#!/usr/bin/env python3
""" List documents """
import pymongo


def list_all(mongo_collection) -> list:
    """ Lists all documents in a collection
        Args:
            mongo_collection: Collection of object

        Return:
            List with documents, otherwise []
    """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

<<<<<<< HEAD
    return documents
=======
    return documents
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
