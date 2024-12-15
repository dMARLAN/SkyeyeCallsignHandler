from typing import Final

import pytest

from services.callsign_handler.callsign_handler import CallsignHandler
from services.callsign_handler.contracts import CallsignRequest, Callsign
from services.callsign_handler.exceptions import EmptyCallsignsException

AA11: Final[Callsign] = Callsign("AA", 1, 1)
AA12: Final[Callsign] = Callsign("AA", 1, 2)

AA21: Final[Callsign] = Callsign("AA", 2, 1)
AA22: Final[Callsign] = Callsign("AA", 2, 2)

BB11: Final[Callsign] = Callsign("BB", 1, 1)


def test_callsign_handler_single_callsign_returns():
    response = CallsignHandler(
        CallsignRequest(
            reference_callsigns=[AA11],
            all_callsigns=[AA11, AA12, BB11]
        )
    ).process_request()

    assert response == "AA 11"


def test_callsign_handler_grouped_callsigns_no_conflicts():
    response = CallsignHandler(
        CallsignRequest(
            reference_callsigns=[AA11, AA12],
            all_callsigns=[AA11, AA12]
        )
    ).process_request()

    assert response == "AA"


def test_callsign_handler_grouped_callsigns_with_conflicts_returns_flight_lead():
    response = CallsignHandler(
        CallsignRequest(
            reference_callsigns=[AA11, AA12],
            all_callsigns=[AA11, AA12, AA21, AA22]
        )
    ).process_request()

    assert response == "AA 11 FLIGHT"


def test_callsign_request_missing_reference_callsigns_raises_exception():
    with pytest.raises(EmptyCallsignsException) as ece:
        CallsignHandler(
            CallsignRequest(
                reference_callsigns=[],
                all_callsigns=[AA11, AA12, BB11]
            )
        ).process_request()

    assert str(ece.value) == "reference_callsigns must be provided"


def test_callsign_request_missing_all_callsigns_raises_exception():
    with pytest.raises(EmptyCallsignsException) as ece:
        CallsignHandler(
            CallsignRequest(
                reference_callsigns=[AA11],
                all_callsigns=[]
            )
        ).process_request()

    assert str(ece.value) == "all_callsigns must be provided"
