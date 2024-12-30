# utils/time.py


import pytz


# Central time
CENTRAL_TZ = pytz.timezone("America/Chicago")  # UTC-6/UTC-5 with DST


def to_central_naive(dt):
    """Convert any datetime to Central time and remove tz info."""
    return dt.astimezone(CENTRAL_TZ).replace(tzinfo=None)
