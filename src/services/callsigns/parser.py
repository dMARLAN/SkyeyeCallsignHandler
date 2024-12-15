import re
from typing import Match

from services.callsigns.constants import GOOD_CALLSIGN_REGEX_PATTERN
from services.callsigns.contracts import Callsign
from services.callsigns.exceptions import InvalidCallsignException


class CallsignParser:
    def __init__(self, callsign: str):
        self.__callsign = callsign

    def parse(self) -> Callsign:
        match = re.match(GOOD_CALLSIGN_REGEX_PATTERN, self.__callsign)

        if not match:
            # Skyeye should catch and respond with invalid callsign.
            # Request: "Skyeye, ;DROP TABLE aircraft, bogey dope"
            # Response: "Invalid callsign."
            raise InvalidCallsignException(f"Invalid callsign: {self.__callsign}")

        flight_name = match.group(1)
        digits = match.group(2).replace("-", "")

        if len(digits) == 2:
            return self.__handle_standard_nato_callsign(flight_name, digits)

        return self.__handle_non_standard_callsign(flight_name, digits)

    @staticmethod
    def __handle_standard_nato_callsign(flight_name: str, digits: str) -> Callsign:
        return Callsign(
            flight_name,
            int(digits[0]),
            int(digits[1]),
        )

    @staticmethod
    def __handle_non_standard_callsign(flight_name: str, digits: str) -> Callsign:
        return Callsign(
            flight_name,
            None,
            int(digits),
        )
