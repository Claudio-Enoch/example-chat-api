from datetime import datetime, timedelta
from flask import jsonify, abort, request, make_response
from flask_restx import Namespace, Resource
from app.models import Message as DbMessage
from app.models import User as DbUser

messages_namespace = Namespace(name="MeSsAgEs", description="*** MESSAGE DESCRIPTION **")


class Messages(Resource):
    parser = messages_namespace.parser()
    parser.add_argument("recipient_id", type=int, required=True, help="Message's recipient_id")
    parser.add_argument("author_id", type=int, required=False, help="Message's author_id")
    parser.add_argument("page", type=int, required=False, help="Pagination of messages")

    @messages_namespace.expect(parser, validate=True)
    def get(self):
        """
        Get all messages to a given author
        responses are limited to 100 per page
        messages are limited to the last 30 days
        """
        args = Messages.parser.parse_args()
        recipient_id, author_id, page = args["recipient_id"], args.get("author_id"), args.get("page", 1)
        page_size = 100
        delta_30_days = datetime.utcnow() - timedelta(days=30)
        if author_id:
            message = (
                DbMessage.query.filter_by(recipient_id=recipient_id, author_id=author_id)
                .filter(DbMessage.created_date > delta_30_days)
                .paginate(page, page_size, error_out=False)
                .items
            )
        else:
            message = (
                DbMessage.query.filter_by(recipient_id=recipient_id)
                .filter(DbMessage.created_date > delta_30_days)
                .paginate(page, page_size, error_out=False)
                .items
            )
        return jsonify(message)

    @messages_namespace.response(400, "validation_error")
    @messages_namespace.response(404, "resource_not_found")
    def post(self):
        """
        - POST /messages
          - { message: STR, author: INT, recipient: INT} -> { message: STR, author: INT, recipient: INT}
        """
        payload = request.get_json(force=True)
        if not all(
            [
                content := payload.get("content"),
                author_id := payload.get("author_id"),
                recipient_id := payload.get("recipient_id"),
            ]
        ):
            abort(400, "validation_error")
        DbUser.query.filter_by(id=author_id).first_or_404("resource_not_found")
        DbUser.query.filter_by(id=recipient_id).first_or_404("resource_not_found")
        message = DbMessage(author_id=author_id, recipient_id=recipient_id, content=content)
        message.create()
        return make_response(jsonify(message), 201)


messages_namespace.add_resource(Messages, "")
