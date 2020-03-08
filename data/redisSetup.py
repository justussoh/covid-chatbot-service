import redis
import requests
import os

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port)

def setupRedis(response):
    cacheKeys = [key['name'] for key in response['fields'][0:3]]
    try:
        for datum in response['features']:
            if datum['attributes']['Province_State'] is None:
                cacheKey = datum['attributes']['Country_Region']
            else:
                cacheKey = f"{datum['attributes']['Country_Region']} {datum['attributes']['Province_State']}"
            for key, value in datum['attributes'].items():
                if key in cacheKeys: continue
                print(f'cacheKey: {cacheKey} \t key: {key}\t value: {value}')
                redis_client.hset(cacheKey, key, value)
        return true
    except Exception as inst:
        print(f'redis setup error {inst}')
        return false

# result
#     feature
#     attribute
#         Province_State, Country_Region, Last_Update, Lat, Long_, Confirmed, Deaths, Recovered