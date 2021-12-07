from flask_restx import Namespace, Resource

messages_namespace = Namespace(name="MeSsAgEs", description="*** MESSAGE DESCRIPTION **")


class Messages(Resource):
    def get(self):
        """
        - GET /messages?author=<user_id>&recipient=<user_id>&days=30&PAGE=1
          - URL:   AUTHOR     STR OPTIONAL
          - PARAM: RECIPIENT  STR OPTIONAL
          - PARAM: DAYS       INT OPTIONAL default=30
          - PARAM: PAGE       INT OPTIONAL default=1 # @page display 100 messages
          - {id: INT, message: STR
        """
        return "GET /messages"

    def post(self):
        """
        - POST /messages
          - { message: STR, author: STR, recipient: STR} -> { message: STR, author: STR, recipient: STR}
        """
        return "POST /messages"


messages_namespace.add_resource(Messages, "")
