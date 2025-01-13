from typing import Final

from services.callsigns.contracts import CallsignRequest, Callsign
from services.callsigns.request_handler import CallsignRequestHandler

AA11: Final[Callsign] = Callsign("AA", 1, 1)
AA12: Final[Callsign] = Callsign("AA", 1, 2)

AA1: Final[Callsign] = Callsign("AA", None, 1)
AA2: Final[Callsign] = Callsign("AA", None, 2)

AA123: Final[Callsign] = Callsign("AA", None, 123)
AA456: Final[Callsign] = Callsign("AA", None, 456)

AA21: Final[Callsign] = Callsign("AA", 2, 1)
AA22: Final[Callsign] = Callsign("AA", 2, 2)

BB11: Final[Callsign] = Callsign("BB", 1, 1)


def test_callsign_handler_single_callsign_standard_nato_returns_full_name():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA11],
            all_callsigns=[BB11]
        )
    ).process_request()

    assert response == "AA 11"


def test_callsign_handler_single_callsign_non_standard_returns_full_name():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA1],
            all_callsigns=[AA1]
        )
    ).process_request()

    assert response == "AA 1"

    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA123],
            all_callsigns=[AA123]
        )
    ).process_request()

    assert response == "AA 123"


def test_callsign_handler_grouped_callsigns_standard_nato_no_conflicts_returns_flight_name():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA11, AA12],
            all_callsigns=[AA11, AA12]
        )
    ).process_request()

    assert response == "AA"


def test_callsign_handler_grouped_callsigns_non_standard_style_no_conflicts_returns_flight_name():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA1, AA2],
            all_callsigns=[AA1, AA2]
        )
    ).process_request()

    assert response == "AA"

    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA123, AA456],
            all_callsigns=[AA123, AA456]
        )
    ).process_request()

    assert response == "AA"


def test_callsign_handler_grouped_callsigns_standard_nato_with_conflicts_returns_flight_lead_flight():
    response = CallsignRequestHandler(
        CallsignRequest(
            reference_callsigns=[AA11, AA12],
            all_callsigns=[AA11, AA12, AA21, AA22]
        )
    ).process_request()

    assert response == "AA 11 FLIGHT"
