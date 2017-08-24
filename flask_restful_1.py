#!/usr/bin/env python3
# -*- utf-8 -*-
#
# https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 24 August, 2017

"""
荷塘月色

$ ./flask_restful_1.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 157-371-811
127.0.0.1 - - [24/Aug/2017 17:29:52] "GET / HTTP/1.1" 200 -

==============================================================================

$ curl http://127.0.0.1:5000
{
    "hello": "world"
}
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
