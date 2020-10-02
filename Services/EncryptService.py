from cryptography.fernet import Fernet
from Entities.User import UserDetails


class EncryptService:

    @classmethod
    def key_generation(cls):
        list_of_keys = []
        key = Fernet.generate_key()
        generated_key = Fernet(key)
        list_of_keys.append(generated_key)
        return generated_key

    @classmethod
    def convert_data_into_encrypt(cls, firstName, lastName, mobile, email_address, password):
        message = [firstName, lastName, mobile, password]
        encrypted_data = []
        key = cls.key_generation()
        for val in message:
            encode_data = val.encode()
            encrypted_value = key.encrypt(encode_data)
            encrypted_data.append(encrypted_value)
        data = UserDetails(encrypted_data[0], encrypted_data[1], encrypted_data[2], email_address,
                           encrypted_data[3])



        #decrypted_message = key.decrypt(encrypted_message)
        #print(encrypted_data)
        return data


