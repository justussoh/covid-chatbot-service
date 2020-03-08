import falcon

from api.endpoints.ok import OK

app = falcon.API(middleware=[])

app.add_route('/', OK())
