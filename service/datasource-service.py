from flask import Flask, request, Response
import cherrypy
from datetime import datetime, timedelta
import json

app = Flask(__name__)

class DataAccess:
    def __init__(self):
        self._entities = []
        now = datetime.now()
        for i in range(0, 10):
            self._entities.append(
                { "_id" : "entity-" + str(i),
                  "name" : "entity " + str(i),
                  "_updated" : "%sZ" % (now + timedelta(microseconds=i)).isoformat()
                })

    def get_entities(self, since):
        if since is None:
            return self._entities
        else:
            return [entity for entity in self._entities if entity["_updated"] > since]

data_access_layer = DataAccess()

@app.route('/entities')
def get_entities():
    since = request.args.get('since')
    entities = data_access_layer.get_entities(since)
    return Response(json.dumps(entities), mimetype='application/json')

if __name__ == '__main__':
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
