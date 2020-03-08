import falcon
from api.db.dbInit import dbInit 

from api.endpoints.ok import OK
from api.endpoints.chat import Chat
from api.endpoints.quarantine import Quarantine

# Create tables necessary.
dbInit()

app = falcon.API(middleware=[])

app.add_route('/', OK())
app.add_route('/chat', Chat())
app.add_route('/quarantine', Quarantine())
