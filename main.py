import falcon

from api.endpoints.ok import OK
from api.endpoints.chat import Chat
from api.endpoints.quarantine import Quarantine

app = falcon.API(middleware=[])

app.add_route('/', OK())
app.add_route('/chat', Chat())
app.add_route('/quarantine', Quarantine())
