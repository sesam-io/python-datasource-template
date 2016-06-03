==========================
python-datasource-template
==========================

A python micro service template for feeding a JSON entity stream to a Sesam service instance.

::

  $ python3 service/datasource-service.py
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5000. JSON entities can be retrieved from 'http://localhost:5000/entities'.

::
   
  $ curl -s 'http://localhost:5000/entities' | python3 -m json.tool
  [
      {
          "_updated": "2016-06-03T14:13:23.296816",
          "_id": "entity-0",
          "name": "entity 0"
      },
      {
          "_updated": "2016-06-03T14:13:23.296827",
          "_id": "entity-1",
          "name": "entity 1"
      },
      {
          "_updated": "2016-06-03T14:13:23.296830",
          "_id": "entity-2",
          "name": "entity 2"
      },
      {
          "_updated": "2016-06-03T14:13:23.296833",
          "_id": "entity-3",
          "name": "entity 3"
      },
      {
          "_updated": "2016-06-03T14:13:23.296836",
          "_id": "entity-4",
          "name": "entity 4"
      },
      {
          "_updated": "2016-06-03T14:13:23.296839",
          "_id": "entity-5",
          "name": "entity 5"
      },
      {
          "_updated": "2016-06-03T14:13:23.296842",
          "_id": "entity-6",
          "name": "entity 6"
      },
      {
          "_updated": "2016-06-03T14:13:23.296845",
          "_id": "entity-7",
          "name": "entity 7"
      },
      {
          "_updated": "2016-06-03T14:13:23.296848",
          "_id": "entity-8",
          "name": "entity 8"
      },
      {
          "_updated": "2016-06-03T14:13:23.296851",
          "_id": "entity-9",
          "name": "entity 9"
      }
  ]

::

  $ curl -s 'http://localhost:5000/entities?since=2016-06-03T14:13:23.296848' | python3 -m json.tool
  [
      {
          "_updated": "2016-06-03T14:13:23.296848",
          "_id": "entity-8",
          "name": "entity 8"
      },
      {
          "_updated": "2016-06-03T14:13:23.296851",
          "_id": "entity-9",
          "name": "entity 9"
      }
  ]
