from .connection import client

from redis.exceptions import ResponseError


def get_all_hash():
    try:
        keys = client.keys()
        # products = client.mget(keys) # can I use this?

        products = [client.hgetall(name=key) for key in keys]
        print(products)
        return products
    except ResponseError as e:
        print(e)


def save_hash(key: str, data: dict):
    try:
        client.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)


def get_hash(key: str):
    try:
        return client.hgetall(name=key)
    except ResponseError as e:
        print(e)


def delete_hash(key: str, keys: list):
    try:
        client.hdel(key, *keys)
    except ResponseError as e:
        print(e)
