from werkzeug.exceptions import BadRequest

from Entities.User import UserDetails
from Constants import UrlConstants as cons

constants = cons.UrlConstants()


class DupCheckForEmailId:

    @classmethod
    def check_email_existing_in_db(cls, email_address):
        data = {}
        if email_address is not None:
            user_details = UserDetails.query.filter_by(email_address=email_address).first()
            if user_details is not None:
                data.update(dict(ResponseText=constants.MAIL_ID_EXITS))
            else:
                data.update(dict(ResponseText=constants.MAIL_ID_NOT_EXITS))
            return data
        raise BadRequest('Invalid email_address')
