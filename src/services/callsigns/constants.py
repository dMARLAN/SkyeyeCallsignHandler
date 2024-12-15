import re
from typing import Final, Pattern

GROUPED_FLIGHT_SUFFIX: Final[str] = "FLIGHT"
GOOD_CALLSIGN_REGEX_PATTERN: Final[Pattern] = re.compile(r"^([A-Z]+) (\d+-?\d*)$")
