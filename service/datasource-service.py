from flask import Flask, request, Response
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
    app.run(debug=True, host='0.0.0.0')

