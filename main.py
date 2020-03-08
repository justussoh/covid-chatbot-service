import falcon

from api.endpoints.ok import OK
from api.endpoints.chat import Chat

app = falcon.API(middleware=[])

app.add_route('/', OK())
app.add_route('/chat', Chat())
