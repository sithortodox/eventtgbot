from datetime import datetime, timedelta
import pytz

def get_date_picker(start_date=None, end_date=None, days_range=7):
    if not start_date:
        start_date = datetime.now()

    if not end_date:
        end_date = start_date + timedelta(days=days_range)

    dates = []
    current_date = start_date

    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    return dates

def localize_datetime(dt, timezone):
    local_timezone = pytz.timezone(timezone)
    return dt.astimezone(local_timezone)
