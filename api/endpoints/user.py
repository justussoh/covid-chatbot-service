import falcon
from datetime import datetime
import api.db.db_methods as db
import json

class User:
    # Return user based on session_id
    def on_get(self, req, resp):
        session_id = req.params.get('session_id')
        query = "SELECT * FROM users WHERE session_id = '{}'".format(session_id)
        user_id, session_id, name, created_at, checked_in, quarantine_duration  = db.fetch_query(query)[0]
        
        if checked_in is not None:
            checked_in = checked_in.strftime("%d %b %Y ")

        resp.status = falcon.HTTP_200
        resp.media = {
            "user_id": user_id,
            "session_id": session_id,
            "name": name,
            "checked_in": checked_in,
            "quarantine_duration": quarantine_duration
        }

    # Create user (TODO: Customize this as necessary to accommodate dialogflow)
    def on_post(self, req, resp):
        data = req.media
        session_id = data['session_id']
        name = data['name']

        query = "INSERT INTO users (session_id,name) VALUES ( '{}', '{}')".format(session_id, name)
        
        db.insert_query(query)
        resp.status = falcon.HTTP_200
        resp.media = ('User created.')