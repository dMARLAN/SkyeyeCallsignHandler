from dataclasses import dataclass
from typing import List, Optional

from services.callsigns.exceptions import EmptyCallsignsException


@dataclass(frozen=True)
class Callsign:
    flight_name: str
    flight_number: Optional[int]
    dash_number: int

    @property
    def full_callsign(self) -> str:
        if self.flight_number:
            return f"{self.flight_name} {self.flight_number} {self.dash_number}"
        return f"{self.flight_name} {self.dash_number}"


@dataclass(frozen=True)
class CallsignRequest:
    reference_callsigns: List[Callsign]
    all_callsigns: List[Callsign]

    def __post_init__(self):
        if not self.reference_callsigns:
            raise EmptyCallsignsException("reference_callsigns must be provided")

        if not self.all_callsigns:
            raise EmptyCallsignsException("all_callsigns must be provided")