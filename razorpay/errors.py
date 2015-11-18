class RazorpayError(Exception):
    """Base Razorpay error class"""
    def __init__(self, status=None, response=None):
        self.status = status
        self.response = response


class BadRequestError(RazorpayError):
    def __init__(self, response=None):
        super(BadRequestError, self).__init__(
            status=400,
            response=response
        )


class NoAuthorizationError(RazorpayError):
    def __init__(self, response=None):
        super(NoAuthorizationError, self).__init__(
            status=401,
            response=response
        )


class NotFoundError(RazorpayError):
    def __init__(self, response=None):
        super(NotFoundError, self).__init__(
            status=404,
            response=response
        )


class ServerError(RazorpayError):
    def __init__(self, response=None):
        status = 500
        if response:
            status = response.status
        super(ServerError, self).__init__(
            status=status,
            response=response
        )
