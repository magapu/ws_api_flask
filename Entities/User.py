from Constants import UrlConstants as const

constants = const.UrlConstants()


class UserDetails:

    def __init__(self, first_name, last_name, mobile, email_address, password, fernet_keys):
        self.firstName = first_name
        self.lastName = last_name
        self.mobile = mobile
        self.email_address = email_address
        self.password = password
        self.fernet_keys = fernet_keys


