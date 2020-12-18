from flask import Flask, request, json
from flask_pymongo import PyMongo
from Constants import UrlConstants as cons
from Services import FetchAllRecordsService as fetchService
from Services import CrudService as crudService
from Services import EncryptService as encryptService
from flask_cors import cross_origin
from Services import LoginService as loginService
from Services import DupCheckForEmailId as dupCheck
from Services import ElasticSearchService as elasticSearch
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'working'

if __name__ == '__main__':
    app.run()
