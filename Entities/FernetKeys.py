from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Constants import UrlConstants as constants

url_constants = constants.UrlConstants()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = url_constants.DATABASE_URL
dataBase = SQLAlchemy(app)


class FernetKeys(dataBase.Model):
    __tablename__ = 'fernet_keys'
    Id = dataBase.Column(dataBase.INTEGER, primary_key=True)
    fernet_keys = dataBase.Column(dataBase.BINARY(255), nullable=False)

    def __init__(self, fernet_keys):
        self.fernet_keys = fernet_keys


dataBase.create_all()

if __name__ == '__main__':
    app.run()
