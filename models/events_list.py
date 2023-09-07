from models.event import Event
import datetime

event_01 = Event(datetime.date(2023, 8, 5), "Late Night Comedy", 26, "The Stand", "hilarious late night comedy", True)
event_02 = Event(datetime.date(2023, 8, 12), "Magic Show", 48, "Underbelly", "magical fun for all the family", False)
event_03 = Event(datetime.date(2023, 8, 20), "The Lady Boys of Bangkok", 135, "Usher Hall", "sparkly dance show", True)

events = [event_01, event_02, event_03]

def add_new_event(event):
    events.append(event)