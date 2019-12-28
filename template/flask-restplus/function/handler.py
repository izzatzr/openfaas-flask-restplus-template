from flask import Flask, request
from flask_restplus import Resource, Api
from __main__ import api

#module_arg = api.parser()
#module_arg.add_argument('',required=True)
@api.route('/<int:module>')
#@api.expect(module_arg)
class resource(Resource):
    def get(self, module):
        return module

    def post(self, module):
        #todos[todo_id] = request.form['data']
        return module

