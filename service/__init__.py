import socket

from quart import Quart

import config.dev as dev_config
import config.pro as pro_config


app = Quart(__name__)

hostname = socket.gethostname()
if hostname == 'PRO-HOSTNAME':
    app.config.from_object(pro_config)
else:
    app.config.from_object(dev_config)


def register():
    from service.v1.urls import v1_bp

    app.register_blueprint(v1_bp)


register()
