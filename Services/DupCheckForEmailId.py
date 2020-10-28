from werkzeug.exceptions import BadRequest

from Entities.User import UserDetails
from Constants import UrlConstants as cons
from Services import EmailService as emailService

constants = cons.UrlConstants()
email_service = emailService.EmailService()


class DupCheckForEmailId:

    @classmethod
    def check_email_existing_in_db(cls, email_address):
        data = {}
        if email_address is not None:
            user_details = UserDetails.query.filter_by(email_address=email_address).first()
            if user_details is not None:
                data.update(dict(ResponseText=constants.MAIL_ID_EXITS))
            else:
                verification_code = email_service.send_verification_mail(email_address)
                data.update(dict(ResponseText=constants.MAIL_ID_NOT_EXITS, VerificationCode=verification_code))
            return data
        raise BadRequest('Invalid email_address')
