#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
<<<<<<< HEAD
print(local_redis.get(key))
=======
print(local_redis.get(key))
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
