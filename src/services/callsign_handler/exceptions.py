class CallsignHandlerException(Exception):
    pass


class NoFlightLeadFoundException(CallsignHandlerException):
    pass


class EmptyReferenceCallsignsException(CallsignHandlerException):
    pass
