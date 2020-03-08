import falcon
from api.db.db_init import dbInit 

from api.endpoints.ok import OK
from api.endpoints.chat import Chat
from api.endpoints.quarantine import Quarantine
from api.endpoints.user import User

# Create tables necessary.
dbInit()

app = falcon.API(middleware=[])

app.add_route('/', OK())
app.add_route('/chat', Chat())
app.add_route('/quarantine', Quarantine())
app.add_route('/user', User())
