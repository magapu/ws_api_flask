from flask import Flask, request
import yaml
from flask_sqlalchemy import SQLAlchemy
from Constants import UrlConstants as cons
from Services import FetchAllRecordsService as fetchService
from Services import CrudService as crudService
from Services import EncryptService as encryptService
from flask_cors import cross_origin
from Services import LoginService as loginService
from Services import DupCheckForEmailId as dupCheck

app = Flask(__name__)
constants = cons.UrlConstants()
yml = yaml.load(open("db.yaml"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
db = SQLAlchemy(app)
fetch_all_rec_ser = fetchService.FetchAllRecordsService()
crud_service = crudService.CrudService()
encrypt_service = encryptService.EncryptService
login_service = loginService.LoginService()
dup_check_for_email_id = dupCheck.DupCheckForEmailId()


@app.route(constants.CHECK_LOGIN_CREDENTIALS, methods=[constants.GET])
@cross_origin(origins="http://localhost:4200")
def user_login_credentials(email_address, user_password):
    return login_service.login_with_credentials(email_address, user_password)


@app.route(constants.CHECK_EMAIL_ID, methods=[constants.GET])
@cross_origin(origins="http://localhost:4200")
def check_email_id(email_address):
    if request.method == constants.GET:
        return dup_check_for_email_id.check_email_existing_in_db(email_address)


@app.route(constants.USER_DETAILS, methods=[constants.POST, constants.GET, constants.PUT, constants.DELETE])
@cross_origin(origins="http://localhost:4200")
def user_details():
    if request.method == constants.POST:
        return crud_service.rec_save(db)

    if request.method == constants.GET:
        return crud_service.fetch_record()

    if request.method == constants.PUT:
        return crud_service.update_rec(db)

    if request.method == constants.DELETE:
        return crud_service.delete_rec(db)


@app.route(constants.FETCH_ALL_RECORDS, methods=[constants.GET])
def fetch_all_records():
    if request.method == constants.GET:
        return fetch_all_rec_ser.fetch_all_records_from_db()


if __name__ == '__main__':
    app.run(port=1994, debug=True)
