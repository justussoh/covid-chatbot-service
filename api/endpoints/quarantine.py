import falcon
from api.db.dbInit import dbInit 
from datetime import datetime

import psycopg2 as psy

class Quarantine:
    def __init__(self):
        dbInit()
        
    # Return the remainder of days quarantined
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = ()

    # Check in on quarantine.
    def on_post(self, req, resp):
        todate = datetime.date(datetime.now())
        # get current user, update quarantine date.
        command = """ """

        resp.status = falcon.HTTP_200
        resp.media = ()