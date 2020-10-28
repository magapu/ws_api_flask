import smtplib
from Constants import UrlConstants as cons
import random

constants = cons.UrlConstants


class EmailService:

    @classmethod
    def send_mail_for_user(cls, email_address, first_name, user_password):
        message = 'Dear ' + first_name + ' Congratulations! You have Successfully Registered into my domain. \n Your ' \
                                         'Id ' \
                                         'and Password to login  \n userId: ' + email_address + '\n password: ' + user_password

        cls.mail_service(email_address, message)

    @classmethod
    def send_verification_mail(cls, email_address):
        random_number: int = random.randint(1000, 9999)
        message = 'Please verify your identity. Please use below code to go ahead ' + str(random_number)
        cls.mail_service(email_address, message)
        return random_number

    @classmethod
    def mail_service(cls, receiver, message):
        sender = constants.MYEMAIL
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, 'Sripassword@1994')
            server.sendmail(sender, receiver, message)
        except smtplib.SMTPException as ex:
            print(ex)
