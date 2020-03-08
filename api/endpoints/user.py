import falcon
from datetime import datetime

import psycopg2 as psy

class User:
    # Return user based on user_id
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = ()

    # Create user (TODO: Customize this as necessary to accommodate dialogflow)
    def on_post(self, req, resp):
        req
        resp.status = falcon.HTTP_200
        resp.media = ()