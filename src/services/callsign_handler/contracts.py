from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Callsign:
    flight_name: str
    flight_number: int
    dash_number: int

    @property
    def full_callsign(self) -> str:
        return f"{self.flight_name} {self.flight_number}{self.dash_number}"


@dataclass(frozen=True)
class CallsignRequest:
    reference_callsigns: List[Callsign]
    all_callsigns: List[Callsign]