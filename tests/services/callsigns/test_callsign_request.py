from typing import Final

import pytest

from services.callsigns.contracts import CallsignRequest, Callsign
from services.callsigns.exceptions import EmptyCallsignsException

AA11: Final[Callsign] = Callsign("AA", 1, 1)
AA12: Final[Callsign] = Callsign("AA", 1, 2)

BB11: Final[Callsign] = Callsign("BB", 1, 1)


def test_callsign_request_missing_reference_callsigns_raises_exception():
    with pytest.raises(EmptyCallsignsException) as ece:
        CallsignRequest(
            reference_callsigns=[],
            all_callsigns=[AA11, AA12, BB11]
        )

    assert str(ece.value) == "reference_callsigns must be provided"


def test_callsign_request_missing_all_callsigns_raises_exception():
    with pytest.raises(EmptyCallsignsException) as ece:
        CallsignRequest(
            reference_callsigns=[AA11],
            all_callsigns=[]
        )

    assert str(ece.value) == "all_callsigns must be provided"
