import sys

from services.callsign_handler.constants import GROUPED_FLIGHT_SUFFIX
from services.callsign_handler.contracts import CallsignRequest, Callsign
from services.callsign_handler.exceptions import NoFlightLeadFoundException


class CallsignHandler:
    def __init__(self, request: CallsignRequest):
        self.__reference_callsigns = request.reference_callsigns
        self.__all_callsigns = request.all_callsigns

    def process_request(self):
        if len(self.__reference_callsigns) == 1:
            return self.__reference_callsigns[0].full_callsign

        if self.__is_conflicting_group():
            return self.__get_flight_lead().full_callsign + GROUPED_FLIGHT_SUFFIX

        return self.__reference_callsigns[0].flight_name

    def __is_conflicting_group(self) -> bool:
        reference_callsign = self.__reference_callsigns[0]

        for callsign in self.__all_callsigns:
            if callsign in self.__reference_callsigns:
                continue

            if callsign.flight_name == reference_callsign.flight_name:
                return True

        return False

    def __get_flight_lead(self) -> Callsign:
        maxsize_callsign = Callsign("", sys.maxsize, sys.maxsize)
        flight_lead = maxsize_callsign

        for callsign in self.__reference_callsigns:
            if callsign.dash_number < flight_lead.dash_number:
                flight_lead = callsign

        if flight_lead is maxsize_callsign:
            raise NoFlightLeadFoundException(f"No flight lead found in {self.__reference_callsigns}")

        return flight_lead
