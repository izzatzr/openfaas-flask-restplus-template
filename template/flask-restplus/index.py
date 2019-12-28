from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)

from function.handler import *

if __name__ == '__main__':
    app.run(debug=True)

