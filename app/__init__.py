import logging

import falcon

from app.config import configs
from app.logs import setup_logging
from app.middleware import Crossdomain, JSONTranslator
from app.resources.root import RootResources, RootNameResources


def create_app():
    app = falcon.API(
        middleware=[
            Crossdomain(),
            JSONTranslator()
        ]
    )

    setup_logging(configs.LOG_LEVEL)
    logger = logging.getLogger(configs.APP_NAME)
    setup_routes(app)

    logger.info('Starting app in {} mode'.format(configs.ENV))

    return app


def setup_routes(app):
    app.add_route('/', RootResources())
    app.add_route('/{name}', RootNameResources())

    return app