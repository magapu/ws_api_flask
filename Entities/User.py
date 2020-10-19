from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Constants import UrlConstants as const

constants = const.UrlConstants()
app1 = Flask(__name__)
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app1.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
sql = SQLAlchemy(app1)


class UserDetails(sql.Model):
    __tablename__ = 'user_Info'
    Id = sql.Column(sql.Integer,  primary_key=True)
    firstName = sql.Column(sql.BINARY(255), nullable=False)
    lastName = sql.Column(sql.BINARY(255), nullable=False)
    mobile = sql.Column(sql.BINARY(255), nullable=False)
    email_address = sql.Column(sql.String(255), nullable=False, unique=True)
    password = sql.Column(sql.BINARY(255), nullable=False)

    def __init__(self, first_name, last_name, mobile, email_address, password):
        self.firstName = first_name
        self.lastName = last_name
        self.mobile = mobile
        self.email_address = email_address
        self.password = password

    def setName(self, first_name):
        self.firstName = first_name

    def getName(self):
        return self.firstName


sql.create_all()

if __name__ == '__main__':
    app1.run()
