#!/usr/bin/env python

import json
import random
from api.models.event import EventModel
from api.models.interest import InterestModel
from config._abstract import AbstractConfig

AbstractConfig.set_up_db()

with open('./resources/event_samples.json', 'r') as events_json_file:
    events_data = json.load(events_json_file)
    events_list = []
    for event in events_data:
        events_list.append(EventModel.create_event(event))

with open('./resources/email_samples.json', 'r') as emails_json_file:
    emails_data = json.load(emails_json_file)
    for email_data in emails_data:
        random_events = random.sample(events_list, k=random.choice(range(1, 10)))
        for random_event in random_events:
            InterestModel.create_interest(data=email_data, event=random_event)
