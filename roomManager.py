"""
Functions:

readRoom(rooms_dir, room_name)
readRooms(rooms_dir)

"""

import os
import json
import fh

# TODO: determine whether this is necessary/wanted
class Prompt:
    def __init__(self, prompts_dict):
        self.text = prompts_dict["text"]
        self.requirements = prompts_dict["requirements"]

    def __str__(self):
        return f"Text: {self.text}\nRequirements: {self.requirements}"

class Room:
    def __init__(self, name, json_dict):
        self.name = name.replace(".json", "")
        self.states = json_dict["states"]
        self.interactions = json_dict["interactions"]
        
        self.prompts = json_dict["prompts"]
        #for json_prompt in json_dict["prompts"]:
        #    self.prompts.append(Prompt(json_prompt))

        self.adjacent_rooms = json_dict["adjacent_rooms"]
    
    def __str__(self):
        return f"States:\n{self.states}\n\nInteractions:\n{self.interactions}\n\nPrompts:\n{self.prompts}\n\nAdjacent Rooms:\n{self.adjacent_rooms}"
    
    # Selects the next prompt based on current states
    # Returns a string containing the text to display
    def nextPrompt(self):
        # For each requirement, check if current states match prompt required states
        for prompt in self.prompts:
            if promptFitsState(prompt, self):
                return prompt
        # TODO: raise custom NoPromptFoundError
        print(f"WARNING: no prompt was found to fit required state for room {self.name}")
        return None

    # Returns an array of interactions available based on current states
    def nextInteractions(self):
        interactions = []
        for interaction in self.interactions:
            if interactionFitsState(interaction, self):
                interactions.append(interaction)
        return interactions

# Returns boolean indicating whether the prompt meets state requirements
def promptFitsState(prompt, room):
    for req_state in prompt["requirements"]:
        state_val = readState(req_state, room, rooms)
        #print(req_state, prompt["requirements"][req_state], state_val) # DEBUG
        if prompt["requirements"][req_state] != state_val:
            return False
    return True

# Returns boolean indicating whether the interaction meets state requirements
def interactionFitsState(interaction, room):
    for req_state in interaction["requirements"]:
        state_val = readState(req_state, room, rooms)
        if interaction["requirements"][req_state] != state_val:
            return False
    return True

# Read room file as Room object
def readRoom(rooms_dir, room_name):
    raw_text = fh.read(f"{rooms_dir}/{room_name}")
    json_dict = json.loads(raw_text)
    room = Room(room_name, json_dict)

    return room


# Read all rooms in a directory into a map of string keys (room names) and Room values (room data)
def readRooms(rooms_dir):
    room_map = {}
    for file in os.listdir(rooms_dir):
        if file.endswith(".json"):
            room_map[file.replace(".json", "")] = readRoom(rooms_dir, file)

    return room_map

# Get state value from local, room, or global path
# Examples: "global.ROOM", "lab_room_3.LIGHTS_ON", "LIGHTS_ON"
# state_path is the string path to get the state
# room is the current active room
# rooms_dict is all the rooms to be accessed
def readState(state_path: str, room: Room, rooms_dict: list[Room]):
    split_path = state_path.split(".")
    if len(split_path) > 1:
        if split_path[0] == "global":
            # query global state
            raise NotImplementedError("Need to query global state!")
        else:
            # query room state
            return rooms_dict[split_path[0]].states[split_path[1]]

    else:
        # local path
        return room.states[state_path]

def setState(state_path, room, rooms_dict, states_dict):
    raise NotImplementedError("setState unimplemented!")


# Debug/Testing
rooms = readRooms("rooms")
room: Room = rooms["lab_room_3"]
#print(readState("LIGHTS_ON", room, rooms))
#prompt = room.nextPrompt()
print(room.nextPrompt()["text"])
print(room.nextInteractions())
room.states["LIGHTS_ON"] = False
print("\n")
print(room.nextPrompt()["text"])
print(room.nextInteractions())