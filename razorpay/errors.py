class RazorpayError(Exception):
    """Base Razorpay error class"""
    def __init__(self, status=None, error=None):
        self.status = status
        self.error = error


class BadRequestError(RazorpayError):
    def __init__(self, error=None):
        super(BadRequestError, self).__init__(
            status=400,
            error=error
        )


class NoAuthorizationError(RazorpayError):
    def __init__(self, error=None):
        super(NoAuthorizationError, self).__init__(
            status=401,
            error=error
        )


class NotFoundError(RazorpayError):
    def __init__(self, error=None):
        super(NotFoundError, self).__init__(
            status=404,
            error=error
        )


class ServerError(RazorpayError):
    def __init__(self, error=None):
        status = 500
        if error:
            status = error.status
        super(ServerError, self).__init__(
            status=status,
            error=error
        )
