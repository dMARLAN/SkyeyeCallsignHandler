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

        if len(match.group(2)) == 2:
            return self.__handle_standard_nato_callsign(match)

        return self.__handle_non_standard_callsign(match)

    @staticmethod
    def __handle_standard_nato_callsign(match: Match[str]) -> Callsign:
        return Callsign(
            match.group(1),
            int(match.group(2)[0]),
            int(match.group(2)[1]),
        )

    @staticmethod
    def __handle_non_standard_callsign(match: Match[str]) -> Callsign:
        return Callsign(
            match.group(1),
            None,
            int(match.group(2)),
        )
