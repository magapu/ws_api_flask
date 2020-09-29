import smtplib
from Constants import UrlConstants as cons

constants = cons.UrlConstants


class EmailService:

    @classmethod
    def send_mail_for_user(cls, email_address, firstName, password):
        sender = constants.MYEMAIL
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
