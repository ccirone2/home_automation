# import anvil.secrets
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timedelta
import pytz

central = pytz.timezone("America/Chicago")  # UTC-6/UTC-5 with DST


@anvil.server.callable
def to_central_naive(dt):
  """Convert any datetime to Central time and remove tz info"""

  # Convert to Central time then strip tz info
  return dt.astimezone(central).replace(tzinfo=None)
