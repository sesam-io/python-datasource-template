from flask import Flask, request, Response
import cherrypy
from datetime import datetime, timedelta
import json
import logging
import paste.translogger


app = Flask(__name__)

logger = logging.getLogger("datasource-service")


class DataAccess:
    def __init__(self):
        self._entities = []
        now = datetime.now()
        for i in range(0, 10):
            self._entities.append({
                "_id": "entity-" + str(i),
                "name": "entity " + str(i),
                "_updated": "%sZ" % (now + timedelta(microseconds=i)).isoformat()
            })

    def get_entities(self, since):
        if since is None:
            return self._entities
        else:
            return [entity for entity in self._entities if entity["_updated"] > since]


data_access_layer = DataAccess()


@app.route('/', methods=['GET'])
def root():
    return Response(status=200, response="I am Groot!")


@app.route('/entities')
def get_entities():
    since = request.args.get('since')
    entities = data_access_layer.get_entities(since)
    return Response(json.dumps(entities), mimetype='application/json')


if __name__ == '__main__':
    format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Log to stdout, change to or add a (Rotating)FileHandler to log to a file
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(stdout_handler)

    # Comment these two lines if you don't want access request logging
    app.wsgi_app = paste.translogger.TransLogger(app.wsgi_app, logger_name=logger.name,
                                                 setup_console_handler=False)
    app.logger.addHandler(stdout_handler)

    logger.propagate = False
    logger.setLevel(logging.INFO)

    cherrypy.tree.graft(app, '/')

    # Set the configuration of the web server to production mode
    cherrypy.config.update({
        'environment': 'production',
        'engine.autoreload_on': False,
        'log.screen': True,
        'server.socket_port': 5000,
        'server.socket_host': '0.0.0.0'
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()
