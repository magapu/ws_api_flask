from flask import request,jsonify
from werkzeug.exceptions import BadRequest
from Constants import UrlConstants as cons
from Entities.User import UserDetails
from Services import EmailService as email_service
from Services import EncryptService as encryptService

emailService = email_service.EmailService
constants = cons.UrlConstants
encrypt_Service = encryptService.EncryptService


class CrudService:

    @classmethod
    def rec_save(cls, dataBase):
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        mobile = request.json['mobile']
        email_address = request.json['email_address']
        password = request.json['password']
        data = encrypt_Service.convert_data_into_encrypt(firstName, lastName, mobile, email_address, password)
        dataBase.session.add(data)
        dataBase.session.commit()
        emailService.send_mail_for_user(email_address, firstName, password)
        data = {
            #constants.Id: Id,
            constants.firstName: firstName,
            constants.lastName: lastName,
            constants.MOBILE: mobile,
            constants.EMAIL_ADDRESS: email_address,
            constants.PASSWORD: password
        }
        return jsonify(data)

    @classmethod
    def fetch_record(cls):
        data = {}
        Id = request.json['Id']
        if Id is not None:
            fetch_data = UserDetails.query.filter_by(Id=Id).first()
            if fetch_data is not None:
                data.update(dict(Id=fetch_data.Id, firstName=fetch_data.firstName, lastName=fetch_data.lastName,
                                 mobile=fetch_data.mobile, email_address=fetch_data.email_address,
                                 password=fetch_data.password))
            return data
        raise BadRequest('Invalid User_Id')

    @classmethod
    def update_rec(cls, dataBase):
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        if Id is not None:
            userData = UserDetails.query.filter_by(Id=Id).first()
            userData.firstName = firstName
            dataBase.session.commit()
            return 'Record Updated'
        raise BadRequest('Invalid Request')

    @classmethod
    def delete_rec(cls, dataBase):
        Id = request.json['Id']
        UserDetails.query.filter_by(Id=Id).delete()
        dataBase.session.flush()
        return 'Deleted'
