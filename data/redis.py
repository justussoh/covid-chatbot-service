import os
import redis

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))

connection = redis.Redis(host=redis_host, port=redis_port)
