from flask import request
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
    def rec_save(cls, data_base):
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        mobile = request.json['mobile']
        email_address = request.json['email_address']
        password = request.json['user_password']
        data = encrypt_Service.convert_data_into_encrypt(first_name, last_name, mobile, email_address, password)
        data_base.session.add(data)
        data_base.session.commit()
        emailService.send_mail_for_user(email_address, first_name, password)
        data = {
            constants.firstName: first_name,
            constants.lastName: last_name,
            constants.MOBILE: mobile,
            constants.EMAIL_ADDRESS: email_address,
            constants.PASSWORD: password
        }
        return data

    @classmethod
    def fetch_record(cls):
        data = {}
        email_address = request.json['email_address']
        if email_address is not None:
            fetch_data = UserDetails.query.filter_by(email_address=email_address).first()
            if fetch_data is not None:
                data.update(dict(Id=fetch_data.Id, firstName=fetch_data.firstName, lastName=fetch_data.lastName,
                                 mobile=fetch_data.mobile, email_address=fetch_data.email_address,
                                 password=fetch_data.password))
            return data
        raise BadRequest('Invalid email_address')

    @classmethod
    def update_rec(cls, data_base):
        id = request.json['Id']
        first_name = request.json['first_name']
        if id is not None:
            user_data = UserDetails.query.filter_by(Id=id).first()
            user_data.firstName = first_name
            data_base.session.commit()
            return 'Record Updated'
        raise BadRequest('Invalid Request')

    @classmethod
    def delete_rec(cls, data_base):
        email_address = request.json['email_address']
        del_data = UserDetails.__table__.delete().where(UserDetails.email_address == email_address)
        data_base.session.execute(del_data)
        data_base.session.commit()
        return 'Deleted'
