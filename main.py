from room import Room
from character import Enemy, Friend

# Create rooms
kitchen = Room("Kitchen")
dining_hall = Room("Dining Hall")
ballroom = Room("Ballroom")

# Set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall.set_description("A large room with ornate golden decorations.")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# Link rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Create characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
jane = Friend("Jane", "A friendly skeleton with a warm smile")
jane.set_conversation("Hello, dear friend! Welcome to our humble abode.")

# Set characters in rooms
dining_hall.set_character(dave)
ballroom.set_character(jane)

# Set the starting room
current_room = kitchen

# Print the initial room description
print(current_room.get_description())

# Print a summary of all rooms and their directions
rooms = [kitchen, dining_hall, ballroom]
for room in rooms:
    room.get_details()

while True:
    command = input("> ")  # Get player's movement command
    if command.lower() in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        print(current_room.get_description())
        character = current_room.get_character()
        if character is not None:
            character.describe()
    elif command.lower() == "talk":
        if character is not None:
            character.talk()
        else:
            print("There's no one here to talk to.")
    elif command.lower() == "fight":
        if character is not None:
            print(character.fight())
            break  # End the game
        else:
            print("There's no one here to fight.")
    elif command.lower() == "hug":
        if character is not None and isinstance(character, Friend):
            print(character.hug())
        else:
            print("There's no one here to hug.")
    else:
        print("Invalid command.")