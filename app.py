from flask import Flask, request, jsonify
import yaml
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
from User import UserDetails
from Constants import UrlConstants as cons

app = Flask(__name__)
constants = cons.UrlConstants()
yml = yaml.load(open("db.yaml"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
db = SQLAlchemy(app)


@app.route(constants.USER_DETAILS, methods=[constants.POST, constants.GET, constants.PUT])
def user_details():
    if request.method == constants.POST:
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        data = UserDetails(Id, firstName, lastName)
        db.session.add(data)
        db.session.commit()
        data = {
            constants.Id: Id,
            constants.firstName: firstName,
            constants.lastName: lastName,
        }
        return data
    if request.method == constants.GET:
        data = {}
        Id = request.json['Id']
        if Id is not None:
            fetch_data = UserDetails.query.filter_by(Id=Id).first()
            if fetch_data is not None:
                data.update(dict(Id=fetch_data.Id, firstName=fetch_data.firstName, lastName=fetch_data.lastName))
            return data
        raise BadRequest('Invalid User_Id')
    if request.method == constants.PUT:
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        update_data = dict(firstName=firstName, lastName=lastName)
        if Id is not None:
            UserDetails.query.filter(UserDetails.Id == Id).update(update_data, synchronize_session=False)
            db.session.commit()
            return 'Record Updated'
        raise BadRequest('Invalid Request ')


@app.route(constants.FETCH_ALL_RECORDS, methods=[constants.GET])
def fetch_all_records():
    if request.method == constants.GET:
        res = []
        data = UserDetails.query.all()
        if data is not None:
            for row in data:
                res.append({constants.Id: row.Id, constants.firstName: row.firstName, constants.lastName: row.lastName})
            return jsonify(res)
        return res


if __name__ == '__main__':
    app.run(debug=True)
