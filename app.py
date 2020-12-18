from flask import Flask, request, json
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/test')
def home_page():
    return 'working'

if __name__ == '__main__':
    app.run()
