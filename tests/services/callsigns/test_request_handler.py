from typing import Final

from services.callsigns.contracts import CallsignRequest, Callsign
from services.callsigns.request_handler import CallsignRequestHandler

AA11: Final[Callsign] = Callsign("AA", 1, 1)
AA12: Final[Callsign] = Callsign("AA", 1, 2)

AA21: Final[Callsign] = Callsign("AA", 2, 1)
AA22: Final[Callsign] = Callsign("AA", 2, 2)

BB11: Final[Callsign] = Callsign("BB", 1, 1)


def test_callsign_handler_single_callsign_returns():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA11],
            all_callsigns=[AA11, AA12, BB11]
        )
    ).process_request()

    assert response == "AA 11"


def test_callsign_handler_grouped_callsigns_no_conflicts():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA11, AA12],
            all_callsigns=[AA11, AA12]
        )
    ).process_request()

    assert response == "AA"


def test_callsign_handler_grouped_callsigns_with_conflicts_returns_flight_lead():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA11, AA12],
            all_callsigns=[AA11, AA12, AA21, AA22]
        )
    ).process_request()

    assert response == "AA 11 FLIGHT"
