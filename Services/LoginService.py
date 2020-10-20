from flask import request
from cryptography.fernet import Fernet

from Entities.User import UserDetails


class LoginService:

    @classmethod
    def login_with_credentials(cls):
        list_of_keys = []
        print('Method Invoked')
        email_address = request.json['email_address']
        user_password = request.json['user_password']
        # user_data = UserDetails.query.filter_by(email_address=email_address).first()
        # if user_data is None:
        #     return ""
