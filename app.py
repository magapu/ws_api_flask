from flask import Flask, request, json
from flask_pymongo import PyMongo
from Services import CrudService as crudService

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'working'

if __name__ == '__main__':
    app.run()
