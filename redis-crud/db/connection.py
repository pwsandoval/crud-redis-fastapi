from redis import Redis
from redis.exceptions import ConnectionError


try:
    client = Redis(
        host="127.0.0.1",
        port="6379",
        password="master_password",
        charset="utf-8",
        decode_responses=True,
    )
except ConnectionError as e:
    print(e)
