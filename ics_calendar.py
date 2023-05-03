import requests
from icalendar import Calendar
from datetime import datetime

def get_ics_calendar(url: str) -> Calendar:
    response = requests.get(url)
    response.raise_for_status()
    ics_data = response.text
    calendar = Calendar.from_ical(ics_data)
    return calendar

def get_events_by_date(calendar: Calendar, date: datetime) -> list:
    events = []
    for component in calendar.walk("VEVENT"):
        start_date = component.get("dtstart").dt
        if start_date.date() == date.date():
            events.append({
                "summary": component.get("summary"),
                "start": start_date,
                "end": component.get("dtend").dt
            })
    return events
