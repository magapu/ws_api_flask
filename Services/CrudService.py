from flask import request, Flask
from werkzeug.exceptions import BadRequest
from Constants import UrlConstants as cons
from Entities.User import UserDetails

constants = cons.UrlConstants()


class CrudService:

    @classmethod
    def rec_save(cls, dataBase):
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        data = UserDetails(Id, firstName, lastName)
        dataBase.session.add(data)
        dataBase.session.commit()
        data = {
            constants.Id: Id,
            constants.firstName: firstName,
            constants.lastName: lastName,
        }
        return data

    @classmethod
    def fetch_record(cls):
        data = {}
        Id = request.json['Id']
        if Id is not None:
            fetch_data = UserDetails.query.filter_by(Id=Id).first()
            if fetch_data is not None:
                data.update(dict(Id=fetch_data.Id, firstName=fetch_data.firstName, lastName=fetch_data.lastName))
            return data
        raise BadRequest('Invalid User_Id')

    @classmethod
    def update_rec(cls, dataBase):
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        update_data = dict(firstName=firstName, lastName=lastName)
        if Id is not None:
            UserDetails.query.filter(UserDetails.Id == Id).update(update_data, synchronize_session=False)
            dataBase.session.commit()
            return 'Record Updated'
        raise BadRequest('Invalid Request ')
