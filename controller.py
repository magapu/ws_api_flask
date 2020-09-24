from flask import Flask, request
import yaml
from flask_sqlalchemy import SQLAlchemy
from Constants import UrlConstants as cons
from Services import FetchAllRecordsService  as fetchService
from Services import CrudService as crudServc

app = Flask(__name__)
constants = cons.UrlConstants()
yml = yaml.load(open("db.yaml"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
db = SQLAlchemy(app)
fetch_all_rec_ser = fetchService.FetchAllRecordsService()
crud_service = crudServc.CrudService()


@app.route(constants.USER_DETAILS, methods=[constants.POST, constants.GET, constants.PUT , constants.DELETE])
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
    app.run(debug=True)
