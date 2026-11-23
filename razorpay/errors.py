class RazorpayError(Exception):
    """Base exception for all Razorpay SDK errors."""
    def __init__(self, message=None, *args, **kwargs):
        super(RazorpayError, self).__init__(message)


class BadRequestError(RazorpayError):
    def __init__(self, message=None, *args, **kwargs):
        super(BadRequestError, self).__init__(message)


class GatewayError(RazorpayError):
    def __init__(self, message=None, *args, **kwargs):
        super(GatewayError, self).__init__(message)


class ServerError(RazorpayError):
    def __init__(self, message=None, *args, **kwargs):
        super(ServerError, self).__init__(message)


class SignatureVerificationError(RazorpayError):
    def __init__(self, message=None, *args, **kwargs):
        super(SignatureVerificationError, self).__init__(message)
