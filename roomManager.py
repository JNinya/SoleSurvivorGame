"""
Functions:

readRoom(rooms_dir, room_name)
readRooms(rooms_dir)

"""

import os
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


# Read room file as Room object
def readRoom(rooms_dir, room_name):

    raw_text = fh.read(f"{rooms_dir}/{room_name}")
    json_dict = json.loads(raw_text)
    room = Room(json_dict)

    return room


# Read all rooms in a directory into a map of string keys (room names) and Room values (room data)
def readRooms(rooms_dir):
    room_map = {}
    for file in os.listdir(rooms_dir):
        if file.endswith(".json"):
            room_map[file.replace(".json", "")] = readRoom(rooms_dir, file)

    return room_map