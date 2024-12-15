class CallsignException(Exception):
    pass


class NoFlightLeadFoundException(CallsignException):
    pass


class EmptyCallsignsException(CallsignException):
    pass


class InvalidCallsignException(CallsignException):
    pass
