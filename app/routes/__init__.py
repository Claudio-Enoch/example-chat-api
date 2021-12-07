from flask_restx import Api

from app.routes.messages import messages_namespace
from app.routes.users import users_namespace

api = Api(title="TITLE EXAMPLE", description="*** MAIN DESCRIPTION ***", contact="Claudio", prefix="/api", doc="/")

api.add_namespace(users_namespace, path="/users")
api.add_namespace(messages_namespace, path="/messages")
