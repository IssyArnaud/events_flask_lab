from flask import render_template, Blueprint, request
from models.events_list import events, add_new_event
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='Fringe Events List', events=events)

@events_blueprint.route('/events', methods=["POST"])
def add_event():
    print(request.form)
    date = request.form["date"]
    event_name = request.form["event_name"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    if request.form.get("recurring"):
        recurring = request.form["recurring"]
    else:   
        recurring = False
    new_event = Event(date, event_name, number_of_guests, room_location, description, recurring)
    add_new_event(new_event)
    return "Done"