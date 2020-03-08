import falcon
from datetime import datetime

import psycopg2 as psy
import api.db.db_methods as db
class Quarantine:
    # Return the remainder of days quarantined
    def on_get(self, req, resp):
        session_id = req.params.get('session_id')
        query = "SELECT * FROM users WHERE session_id = '{}'".format(session_id)
        user_id, session_id, name, created_at, checked_in, quarantine_duration  = db.fetch_query(query)[0]

        if checked_in is None:
            resp.media = ('User is not quarantined.')

        todate = datetime.date(datetime.now())
        
        # Compare todate with checked_in date.
        checked_in = datetime.date(checked_in)
        days_past = todate - checked_in
        remainder = quarantine_duration - days_past

        if (remainder < 0):
            query = "SELECT * FROM users WHERE session_id = '{}'".format(session_id)
            # Ensure user is valid
            user = db.fetch_query(query)[0]
            # Checkout user, simple implementation due to time constraint.
            if user:
                query = "UPDATE users SET checked_in = null WHERE session_id = '{}'".format(session_id)
                db.commit_query(query)
        else:
            resp.status = falcon.HTTP_200
            resp.media = ({"remainder": remainder})

        


    # Check in on quarantine.
    def on_post(self, req, resp):
        data = req.media
        session_id = data['session_id']
        todate = datetime.date(datetime.now())
        # get current user, update quarantine date.
        query = "SELECT * FROM users WHERE session_id = '{}'".format(session_id)
        # Ensure user is valid

        user = db.fetch_query(query)[0]

        if user:
            query = "UPDATE users SET checked_in = {} WHERE session_id = '{}'".format(todate, session_id)
            db.commit_query(query)


        resp.status = falcon.HTTP_200
        resp.media = ('User checked in.')