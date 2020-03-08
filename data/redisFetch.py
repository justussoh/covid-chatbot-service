import redis
import requests
import os

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port)
COVID_ENDPOINT = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json"
cheatTotalConfirmed = 0
cheatTotalDeaths = 0
cheatTotalRecovered = 0

def updateRedis():
    global cheatTotalConfirmed
    global cheatTotalDeaths
    global cheatTotalRecovered
    response = requests.get(url=COVID_ENDPOINT).json()
    cacheKeys = [key['name'] for key in response['fields'][0:3]]
    try:
        for datum in response['features']:
            if datum['attributes']['Province_State'] is None:
                cacheKey = datum['attributes']['Country_Region']
            else:
                cacheKey = f"{datum['attributes']['Country_Region']} {datum['attributes']['Province_State']}"
            for key, value in datum['attributes'].items():
                if key in cacheKeys: continue
                if key == "Confirmed":
                    cheatTotalConfirmed += value
                elif key == "Death":
                    cheatTotalDeaths += value
                if key == "Recovered":
                    cheatTotalRecovered += value
                print(f'cacheKey: {cacheKey} \t key: {key}\t value: {value}')
                redis_client.hset(cacheKey, key, value)
        print(f'cheatTotalConfirmed: {cheatTotalConfirmed} \t cheatTotalDeaths: {cheatTotalDeaths}\t cheatTotalRecovered: {cheatTotalRecovered}')
        return True
    except Exception as inst:
        print(f'redis setup error {inst}')
        return False

def getFromRedis(location, field):
    global cheatTotalConfirmed
    global cheatTotalDeaths
    global cheatTotalRecovered
    if location == "all":
        if field == "Confirmed":
            return cheatTotalConfirmed
        elif field == "Deaths":
            return cheatTotalDeaths
        if field == "Recovered":
            return cheatTotalRecovered
    else:
        return redis_client.hget(location, field)


# result
#     feature
#     attribute
#         Province_State, Country_Region, Last_Update, Lat, Long_, Confirmed, Deaths, Recovered