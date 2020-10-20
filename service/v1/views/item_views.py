from uuid import uuid4

from quart.views import MethodView
from quart import request, jsonify


class HandleItemView(MethodView):
    @staticmethod
    async def get():
        _item_id = request.args.get('item_id')

        return jsonify(dict(item_id=_item_id, item_name=uuid4().hex))

    @staticmethod
    async def post():
        return jsonify(dict(method='POST', item_name=uuid4().hex))

    @staticmethod
    async def put():
        return jsonify(dict(method='PUT', item_name=uuid4().hex))

    @staticmethod
    async def patch():
        return jsonify(dict(method='PATCH', item_name=uuid4().hex))

    @staticmethod
    async def delete():
        return jsonify(dict(method='DELETE', item_name=uuid4().hex))
