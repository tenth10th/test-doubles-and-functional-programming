import time
from typing import Dict


DEFAULT_STANDOFF = 5


def handle_rate_limit(api_response: Dict) -> bool:
    """
    If our API response was rate limited, wait for the specified standoff time
    (which is specified as a string, representing seconds to wait, if present)

    Return True if a rate limit occurred, otherwise False
    """
    seconds_str = api_response.get('standoff_time', '')
    seconds_int = None

    try:
        if seconds_str:
            seconds_int = int(seconds_str)
    except (ValueError):
        print(f"Invalid standoff_time? Defaulting to {DEFAULT_STANDOFF} seconds")
        seconds_int = DEFAULT_STANDOFF

    if seconds_int:
        time.sleep(seconds_int)
        return True

    return False
