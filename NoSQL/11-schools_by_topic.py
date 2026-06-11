#!/usr/bin/env python3
""" Where can I learn Python? """
import pymongo


def schools_by_topic(mongo_collection, topic: str):
    """ Search the school based in school

        Args:
            mongo_collection: Collection
            topic: Content

        Return:
            List of school
    """
    query: dict = {"topics": topic}
    schools: list = []

    for school in mongo_collection.find(query):
        schools.append(school)

<<<<<<< HEAD
    return schools
=======
    return schools
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
