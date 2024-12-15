class CallsignHandlerException(Exception):
    pass


class NoFlightLeadFoundException(CallsignHandlerException):
    pass


class EmptyCallsignsException(CallsignHandlerException):
    pass
