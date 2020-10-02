from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Constants import UrlConstants as const

constants = const.UrlConstants()
app1 = Flask(__name__)
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app1.config['SQLALCHEMY_DATABASE_URI'] = constants.DATABASE_URL
sql = SQLAlchemy(app1)


class UserDetails(sql.Model):
    __tablename__ = 'userInfo'
    Id = sql.Column(sql.Integer,  primary_key=True)
    firstName = sql.Column(sql.BINARY(50), nullable=False)
    lastName = sql.Column(sql.BINARY(50), nullable=False)
    mobile = sql.Column(sql.BINARY(50), nullable=False)
    email_address = sql.Column(sql.String(50), nullable=False , unique=True)
    password = sql.Column(sql.BINARY(50), nullable=False)

    def __init__(self,  firstName, lastName, mobile, email_address, password):
        self.firstName = firstName
        self.lastName = lastName
        self.mobile = mobile
        self.email_address = email_address
        self.password = password

    def setName(self, firstName):
        self.firstName = firstName

    def getName(self):
        return self.firstName


sql.create_all()

if __name__ == '__main__':
    app1.run()
