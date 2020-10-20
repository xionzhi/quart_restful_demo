from uuid import uuid4

from quart.views import MethodView
from quart import request, jsonify


class HandleUserView(MethodView):
    @staticmethod
    async def get():
        _user_id = request.args.get('user_id')

        return jsonify(dict(user_id=_user_id, user_name=uuid4().hex))

    @staticmethod
    async def post():
        return jsonify(dict(method='POST', user_name=uuid4().hex))

    @staticmethod
    async def put():
        return jsonify(dict(method='PUT', user_name=uuid4().hex))

    @staticmethod
    async def patch():
        return jsonify(dict(method='PATCH', user_name=uuid4().hex))

    @staticmethod
    async def delete():
        return jsonify(dict(method='DELETE', user_name=uuid4().hex))
