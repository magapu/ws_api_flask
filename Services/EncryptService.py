from cryptography.fernet import Fernet

from Entities.FernetKeys import FernetKeys
from Entities.User import UserDetails


class EncryptService:

    @classmethod
    def key_generation(cls):
        key = Fernet.generate_key()
        return key

    @classmethod
    def convert_data_into_encrypt(cls, first_name, last_name, mobile, email_address, password):
        message = [first_name, last_name, mobile, password]
        encrypted_data = []
        key = cls.key_generation()
        generated_key = Fernet(key)
        for val in message:
            encode_data = val.encode()
            encrypted_value = generated_key.encrypt(encode_data)
            encrypted_data.append(encrypted_value)
        data = UserDetails(encrypted_data[0], encrypted_data[1], encrypted_data[2], email_address,
                           encrypted_data[3], key)
        return data
