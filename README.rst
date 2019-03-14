==========================
python-datasource-template
==========================

A Python micro service template for feeding a JSON entity stream to a Sesam service instance.

::

  $ python3 service/datasource-service.py
  [14/Mar/2019:10:32:40] ENGINE Bus STARTING
  [14/Mar/2019:10:32:40] ENGINE Started monitor thread '_TimeoutMonitor'.
  [14/Mar/2019:10:32:40] ENGINE Serving on http://0.0.0.0:5000
  [14/Mar/2019:10:32:40] ENGINE Bus STARTED

The service listens on port 5000. JSON entities can be retrieved from 'http://localhost:5000/entities'.

::

  $ curl -s 'http://localhost:5000/entities' | python3 -m json.tool
  [
      {
          "name": "entity 0",
          "_id": "entity-0",
          "_updated": "2016-06-26T10:46:13.351467Z"
      },
      {
          "name": "entity 1",
          "_id": "entity-1",
          "_updated": "2016-06-26T10:46:13.351468Z"
      },
      {
          "name": "entity 2",
          "_id": "entity-2",
          "_updated": "2016-06-26T10:46:13.351469Z"
      },
      {
          "name": "entity 3",
          "_id": "entity-3",
          "_updated": "2016-06-26T10:46:13.351470Z"
      },
      {
          "name": "entity 4",
          "_id": "entity-4",
          "_updated": "2016-06-26T10:46:13.351471Z"
      },
      {
          "name": "entity 5",
          "_id": "entity-5",
          "_updated": "2016-06-26T10:46:13.351472Z"
      },
      {
          "name": "entity 6",
          "_id": "entity-6",
          "_updated": "2016-06-26T10:46:13.351473Z"
      },
      {
          "name": "entity 7",
          "_id": "entity-7",
          "_updated": "2016-06-26T10:46:13.351474Z"
      },
      {
          "name": "entity 8",
          "_id": "entity-8",
          "_updated": "2016-06-26T10:46:13.351475Z"
      },
      {
          "name": "entity 9",
          "_id": "entity-9",
          "_updated": "2016-06-26T10:46:13.351476Z"
      }
  ]

::

   curl -s 'http://localhost:5000/entities?since=2016-06-26T10:46:13.351474Z' | python3 -m json.tool
  [
      {
          "name": "entity 8",
          "_id": "entity-8",
          "_updated": "2016-06-26T10:46:13.351475Z"
      },
      {
          "name": "entity 9",
          "_id": "entity-9",
          "_updated": "2016-06-26T10:46:13.351476Z"
      }
  ]
