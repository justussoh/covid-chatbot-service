import requests
import ring.coder
from data.redis import connection

HOURS = 3600
DAYS = HOURS * 24


@ring.redis(connection, coder='json', expire=DAYS)
def fetch_data():
    COVID_ENDPOINT = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(url=COVID_ENDPOINT)
    return response.json()


def filter_data():
    #insert your stuff here
    pass
