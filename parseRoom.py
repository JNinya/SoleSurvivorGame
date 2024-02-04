"""
Functions:

readRoom(room_name)

"""

import json
import fh

class Room:
    def __init__(self, json_dict):
        self.states = json_dict["states"]
        self.interactions = json_dict["interactions"]
        self.prompts = json_dict["prompts"]
        self.adjacent_rooms = json_dict["adjacent_rooms"]
    
    def __str__(self):
        return f"States:\n{self.states}\n\nInteractions:\n{self.interactions}\n\nPrompts:\n{self.prompts}\n\nAdjacent Rooms:\n{self.adjacent_rooms}"



def readRoom(room_name):

    raw_text = fh.read(f"rooms/{room_name}")
    json_dict = json.loads(raw_text)
    room = Room(json_dict)

    return room


print(readRoom("start.json"))