import falcon
from datetime import datetime

import psycopg2 as psy

try:
    conn = psy.connect("dbname='covid' user='admin' host='35.239.162.61' password='12345678'")
except:
    print("Error connecting to database.")

class User:
    # Return user based on user_id
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = ()

    # Create user (TODO: Customize this as necessary to accommodate dialogflow)
    def on_post(self, req, resp):
        data = req.media
        session_id = data['session_id']
        name = data['name']

        query = "INSERT INTO users (session_id,name) VALUES ( '{}', '{}')".format(session_id, name)
        

        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()

        resp.status = falcon.HTTP_200
        resp.media = ('User created.')