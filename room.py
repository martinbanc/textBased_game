class Room():
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None



    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name



    def get_linked_room(self, direction):
        return self.linked_rooms.get(direction)  # Assuming linked_rooms is a dictionary

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        direction = direction.lower()
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character


