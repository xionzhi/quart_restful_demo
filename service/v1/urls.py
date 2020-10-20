from quart import Blueprint

from service.v1.views.user_views import (HandleUserView)
from service.v1.views.item_views import (HandleItemView)

v1_bp = Blueprint('v1', __name__, url_prefix='/api/v1')

v1_bp.add_url_rule('/user', view_func=HandleUserView.as_view('user'))
v1_bp.add_url_rule('/item', view_func=HandleItemView.as_view('item'))
