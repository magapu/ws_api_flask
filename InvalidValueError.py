from http.client import HTTPException


class InvalidValueError(HTTPException):
    code = 406
    pass
