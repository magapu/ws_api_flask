from flask import Flask, request, json
from flask_pymongo import PyMongo
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route('/test')
def home_page():
    return 'working'

if __name__ == '__main__':
    app.run()
