import falcon

from api.endpoints.ok import OK

api = falcon.API(middleware=[])

api.add_route('/', OK())
