from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

class DataAccess:
    def __init__(self):
        self._entities = []
        for i in range(0, 10):
            self._entities.append(
                { "_id" : "entity-" + str(i),
                  "name" : "entity " + str(i),
                  "_updated" : datetime.now().isoformat()
                })

    def get_entities(self, since):
        if since is None:
            return self._entities
        else:
            return [entity for entity in self._entities if entity["_updated"] >= since]

data_access_layer = DataAccess()

@app.route('/entities')
def get_entities():
    since = request.args.get('since')
    entities = data_access_layer.get_entities(since)
    return jsonify(result=entities)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

