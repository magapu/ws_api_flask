from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Constants import UrlConstants as cons
from Services import FetchAllRecordsService as fetchService
from Services import CrudService as crudService
from Services import EncryptService as encryptService
from flask_cors import cross_origin
from Services import LoginService as loginService
from Services import DupCheckForEmailId as dupCheck
from elasticsearch import Elasticsearch
application = Flask(__name__)
constants = cons.UrlConstants()
# yml = yaml.load(open("app.yaml"))
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
db = SQLAlchemy(application)
fetch_all_rec_ser = fetchService.FetchAllRecordsService()
crud_service = crudService.CrudService()
encrypt_service = encryptService.EncryptService
login_service = loginService.LoginService()
dup_check_for_email_id = dupCheck.DupCheckForEmailId()


@application.route('/')
def home_page():
    return 'working'


@application.route('/search', methods=['POST'])
def search():
    email_address = request.json['email_address']
    body = {
        "query": {
            "multi_match": {
                "query": email_address
            }
        }
    }
    es = Elasticsearch('http://localhost:9200/')
    res = es.search(index="srinivas_elasticsearch", doc_type="title", body=body)
    return jsonify(res)


@application.route(constants.CHECK_LOGIN_CREDENTIALS, methods=[constants.GET])
@cross_origin()
def user_login_credentials(email_address, user_password):
    return login_service.login_with_credentials(email_address, user_password)


@application.route(constants.CHECK_EMAIL_ID, methods=[constants.GET])
@cross_origin()
def check_email_id(email_address):
    if request.method == constants.GET:
        return dup_check_for_email_id.check_email_existing_in_db(email_address)


@application.route(constants.USER_DETAILS, methods=[constants.POST, constants.GET, constants.PUT, constants.DELETE])
@cross_origin()
def user_details():
    if request.method == constants.POST:
        return crud_service.rec_save(db)

    if request.method == constants.GET:
        return crud_service.fetch_record()

    if request.method == constants.PUT:
        return crud_service.update_rec(db)

    if request.method == constants.DELETE:
        return crud_service.delete_rec(db)


@application.route(constants.FETCH_ALL_RECORDS, methods=[constants.GET])
@cross_origin()
def fetch_all_records():
    if request.method == constants.GET:
        return fetch_all_rec_ser.fetch_all_records_from_db()


if __name__ == '__main__':
    application.run()
