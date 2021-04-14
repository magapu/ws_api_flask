from flask import request,jsonify
from werkzeug.exceptions import BadRequest
from Constants import UrlConstants as cons
from Entities.User import UserDetails
from Services import EmailService as email_service
from Services import EncryptService as encryptService
from Services import ElasticSearchService as elasticSearch
from cryptography.fernet import Fernet

emailService = email_service.EmailService
constants = cons.UrlConstants
encrypt_Service = encryptService.EncryptService
elasticSearchService = elasticSearch.ElasticSearchService()


class CrudService:

    @classmethod
    def rec_save(cls, user_collection):
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        mobile = request.json['mobile']
        email_address = request.json['email_address']
        password = request.json['user_password']
        data = encrypt_Service.convert_data_into_encrypt(first_name, last_name, mobile, email_address, password)
        try:
            user_collection.insert_one({'first_Name': data.firstName, 'last_name': data.lastName, 'mobile': data.mobile,
                                        'email_address': data.email_address, 'password': data.password,
                                        'key': data.fernet_keys})
            user_data = user_collection.find_one({'email_address': email_address})
            elasticSearchService.insert_data(email_address, user_data['_id'])
            emailService.send_mail_for_user(email_address, first_name, password)
        except Exception as ExInSave:
            raise ExInSave
        data = {
            constants.firstName: first_name,
            constants.lastName: last_name,
            constants.MOBILE: mobile,
            constants.EMAIL_ADDRESS: email_address,
            constants.PASSWORD: password
        }
        return jsonify(data)

    @classmethod
    def fetch_record(cls, user_collection, email_address, showPassword):
        data = {}
        if email_address is not None:
            fetch_data = user_collection.find_one({'email_address': email_address})
            if fetch_data is not None:
                key = Fernet(fetch_data['key'])
                decrypted_first_name = key.decrypt(fetch_data['first_Name'])
                decrypted_last_name = key.decrypt(fetch_data['last_name'])
                decrypted_mobile = key.decrypt(fetch_data['mobile'])
                decrypted_password = key.decrypt(fetch_data['password'])
                decode_first_name = decrypted_first_name.decode()
                decode_last_name = decrypted_last_name.decode()
                decode_mobile = decrypted_mobile.decode()
                decode_password = decrypted_password.decode()
                if showPassword == "True":
                    data.update(dict(firstName=decode_first_name,
                                     lastName=decode_last_name,
                                     mobile=decode_mobile, email_address=fetch_data['email_address'],
                                     password=decode_password))
                else:
                    data.update(dict(firstName=decode_first_name,
                                     lastName=decode_last_name,
                                     email_address=fetch_data['email_address']))

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
    def delete_rec(cls, user_collection, email_address):
        if email_address is not None:
            fetch_data = user_collection.find_one({'email_address': email_address})
            user_collection.delete_one({'email_address': email_address})
            if fetch_data is not None:
                if fetch_data['_id']:
                    elasticSearchService.delete_record(fetch_data['_id'])
        else:
            return BadRequest('Please Enter Valid Email-Id')
        return 'Deleted'
