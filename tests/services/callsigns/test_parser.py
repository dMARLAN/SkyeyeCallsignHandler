import pytest

from services.callsigns.contracts import Callsign
from services.callsigns.exceptions import InvalidCallsignException
from services.callsigns.parser import CallsignParser


def test_parse_standard_nato():
    assert CallsignParser("AA 11").parse() == Callsign("AA", 1, 1)
    assert CallsignParser("FOO 12").parse() == Callsign("FOO", 1, 2)
    assert CallsignParser("AA 1").parse() == Callsign("AA", None, 1)


def test_parse_stupid_usaf_style():
    assert CallsignParser("AA 1").parse() == Callsign("AA", None, 1)


def test_parse_non_nato_callsign():
    assert CallsignParser("AA 123").parse() == Callsign("AA", None, 123)


def test_parser_invalid_callsign():
    with pytest.raises(InvalidCallsignException) as ice:
        CallsignParser("Tom Cruise").parse()
    assert str(ice.value) == "Invalid callsign: Tom Cruise"

    with pytest.raises(InvalidCallsignException) as ice:
        CallsignParser(";DROP TABLE aircraft").parse()
    assert str(ice.value) == "Invalid callsign: ;DROP TABLE aircraft"
