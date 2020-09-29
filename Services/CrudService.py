from flask import request
from werkzeug.exceptions import BadRequest
from Constants import UrlConstants as cons
from Entities.User import UserDetails
import smtplib

constants = cons.UrlConstants()


class CrudService:

    @classmethod
    def rec_save(cls, dataBase):
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        mobile = request.json['mobile']
        email_address = request.json['email_address']
        password = request.json['password']
        data = UserDetails(Id, firstName, lastName, mobile, email_address, password)
        dataBase.session.add(data)
        cls.send_mail_for_user(email_address, firstName, password)
        dataBase.session.commit()
        data = {
            constants.Id: Id,
            constants.firstName: firstName,
            constants.lastName: lastName,
            constants.MOBILE: mobile,
            constants.EMAIL_ADDRESS: email_address,
            constants.PASSWORD: password
        }
        return data

    @classmethod
    def fetch_record(cls):
        data = {}
        Id = request.json['Id']
        if Id is not None:
            fetch_data = UserDetails.query.filter_by(Id=Id).first()
            if fetch_data is not None:
                data.update(dict(Id=fetch_data.Id, firstName=fetch_data.firstName, lastName=fetch_data.lastName))
            return data
        raise BadRequest('Invalid User_Id')

    @classmethod
    def update_rec(cls, dataBase):
        Id = request.json['Id']
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        if Id is not None:
            userData = UserDetails.query.filter_by(Id=Id).first()
            userData.firstName = firstName
            dataBase.session.commit()
            return 'Record Updated'
        raise BadRequest('Invalid Request')

    @classmethod
    def delete_rec(cls, dataBase):
        Id = request.json['Id']
        UserDetails.query.filter_by(Id=Id).delete()
        dataBase.session.flush()
        return 'Deleted'

    @classmethod
    def send_mail_for_user(cls, email_address, firstName, password):
        sender = cons.UrlConstants.MYEMAIL
        receiver = email_address
        message = 'Dear ' + firstName + 'Congratulations! You have Successfully Registered into my domain. \n Your Id ' \
                                        'and Passwords to login  \n userId: ' + email_address + '\n password: ' + password
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, 'Sripassword@1994')
            server.sendmail(sender, receiver, message)
            return 'mail sent successful'
        except smtplib.SMTPException as ex:
            print(ex)
