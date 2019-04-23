class AppException(Exception):
    """
    Base exception for application that accepts text or an exception inherited
    from this class
    """

    def __init__(self, message=None):
        self.message = str(message)


class HTTPError(AppException):
    def __init__(self, message='Error', code=None):
        super().__init__(message)
        self.code = code


class BadRequest(HTTPError):
    def __init__(self, message='Bad Request', code=400):
        super().__init__(message, code)
