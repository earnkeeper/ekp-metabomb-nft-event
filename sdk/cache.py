import json

import redis
from decouple import config

r = redis.Redis(
    host=config("REDIS_HOST", default="localhost"),
    port=config("REDIS_PORT", default=6379, cast=int),
    db=config("REDIS_DB", default=0, cast=int),
    password=config("REDIS_PASSWORD", default=None)
)

def get(key):
    value = r.get(key)
    if (value is None):
        return None
    return json.loads(value)


def set(key, value):
    if (set is not None):
        return r.set(key, json.dumps(value))
    return r.set(key, value)
