from models.event import Event

event_01 = Event("05/08/2023", "Late Night Comedy", 26, "The Stand", "hilarious late night comedy", True)
event_02 = Event("12/08/2023", "Magic Show", 48, "Underbelly", "magical fun for all the family", False)
event_03 = Event("20/08/2023", "The Lady Boys of Bangkok", 135, "Usher Hall", "sparkly dance show", True)

events = [event_01, event_02, event_03]

def add_new_event(event):
    events.append(event)