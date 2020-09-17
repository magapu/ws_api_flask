from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app1 = Flask(__name__)
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app1.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost:1995/sridb'
sql = SQLAlchemy(app1)


class UserDetails(sql.Model):
    sequenceNumber = sql.Column(sql.Integer, primary_key=True)
    Id = sql.Column(sql.Integer , nullable=False,unique=True)
    firstName = sql.Column(sql.String(50), nullable=False)
    lastName = sql.Column(sql.String(50), nullable=False)

    def __init__(self, Id, firstName, lastName):
        self.Id = Id
        self.firstName = firstName
        self.lastName = lastName

    def setName(self, firstName):
        self.firstName = firstName

    def getName(self):
        return self.firstName


sql.create_all()

if __name__ == '__main__':
    app1.run()
