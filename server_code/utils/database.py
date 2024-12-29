# nest_monitor/db_utils.py
import anvil.tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta


def save_temperature_reading(temperature):
    """Save a temperature reading to the database"""
    app_tables.temperature_readings.add_row(timestamp=datetime.now(), temperature=temperature)


def cleanup_old_readings():
    """Remove readings older than 7 days"""
    week_ago = datetime.now() - timedelta(days=7)
    old_rows = app_tables.temperature_readings.search(timestamp=q.less_than(week_ago))
    for row in old_rows:
        row.delete()


def get_temperature_readings(start_time, end_time):
    """Fetch temperature readings between start_time and end_time"""
    return app_tables.temperature_readings.search(timestamp=q.between(start_time, end_time))
