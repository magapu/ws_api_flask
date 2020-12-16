from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from Constants import UrlConstants as cons
from Services import FetchAllRecordsService as fetchService
from Services import CrudService as crudService
from Services import EncryptService as encryptService
from flask_cors import cross_origin
from Services import LoginService as loginService
from Services import DupCheckForEmailId as dupCheck
from Services import ElasticSearchService as elasticSearch

application = Flask(__name__)
constants = cons.UrlConstants()
# yml = yaml.load(open("app.yaml"))
# application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# application.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
application.config["MONGO_URI"] = constants.DATABASE_URL
mongo = PyMongo(application)
fetch_all_rec_ser = fetchService.FetchAllRecordsService()
crud_service = crudService.CrudService()
encrypt_service = encryptService.EncryptService
login_service = loginService.LoginService()
dup_check_for_email_id = dupCheck.DupCheckForEmailId()
elasticSearchService = elasticSearch.ElasticSearchService
user_collection = mongo.db.usersDetails


@application.route('/')
def home_page():
    return 'working'


@application.route('/search/<string:_query>', methods=[constants.GET])
@cross_origin()
def search(_query):
    return elasticSearchService.search_data(_query)


@application.route('/deleteRecInEs/<user_id>', methods=[constants.DELETE])
@cross_origin()
def delete_rec_in_es(user_id):
    elasticSearchService.delete_record(user_id)
    return 'Deleted'


@application.route(constants.CHECK_LOGIN_CREDENTIALS, methods=[constants.GET])
@cross_origin()
def user_login_credentials(email_address, user_password):
    return login_service.login_with_credentials(email_address, user_password, user_collection)


@application.route(constants.CHECK_EMAIL_ID, methods=[constants.GET])
@cross_origin()
def check_email_id(email_address):
    if request.method == constants.GET:
        return dup_check_for_email_id.check_email_existing_in_db(email_address, user_collection)


@application.route('/fetchUserDetail/<string:email_address>/<string:showPassword>', methods=['GET'])
@cross_origin()
def fetch_user_details(email_address, showPassword):
    return crud_service.fetch_record(user_collection, email_address, showPassword)


@application.route(constants.USER_DETAILS, methods=[constants.POST, constants.GET, constants.PUT, constants.DELETE])
@cross_origin()
def user_details():
    if request.method == constants.POST:
        return crud_service.rec_save(user_collection)

    if request.method == constants.PUT:
        return crud_service.update_rec(user_collection)

    if request.method == constants.DELETE:
        return crud_service.delete_rec(user_collection)


@application.route(constants.FETCH_ALL_RECORDS, methods=[constants.GET])
@cross_origin()
def fetch_all_records():
    if request.method == constants.GET:
        return fetch_all_rec_ser.fetch_all_records_from_db()


if __name__ == '__main__':
    application.run()
