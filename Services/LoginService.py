from flask import request
from cryptography.fernet import Fernet
from Entities.User import UserDetails
from Services import CrudService as crudService
from Constants import UrlConstants as constants
from http import HTTPStatus
crud_service = crudService.CrudService()
url_constants = constants.UrlConstants()


class LoginService:

    @classmethod
    def login_with_credentials(cls, email_address, user_password):
        res = {}
        fetch_user_data = UserDetails.query.filter_by(email_address=email_address).first()
        if fetch_user_data is not None:
            key = Fernet(fetch_user_data.fernet_keys)
            decrypted_password = key.decrypt(fetch_user_data.password)
            decode_password = decrypted_password.decode()
            if decode_password == user_password:
                res = {
                    url_constants.ResponseText: HTTPStatus.OK
                }
            else:
                res = {
                    url_constants.ResponseText: HTTPStatus.UNAUTHORIZED
                }
        else:
            res = {
                url_constants.ResponseText: HTTPStatus.NOT_FOUND
            }

        return res
